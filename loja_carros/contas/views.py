from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import authenticate, login

from .serializers import AdministradorSerializer, VendedorSerializer, ClienteSerializer
from .models import User

# Registro
class AdministradorRegistrationView(APIView):
    def post(self, request):
        serializer = AdministradorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VendedorRegistrationView(APIView):
    def post(self, request):
        serializer = VendedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClienteRegistrationView(APIView):
    def post(self, request):
        serializer = ClienteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Login (separado por perfil)
class AdministradorLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.tipo == 'admin':
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'username': user.username,
                'tipo': user.tipo,
            })
        return Response({'error': 'Credenciais inválidas ou usuário não é admin'}, status=status.HTTP_401_UNAUTHORIZED)

class VendedorLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.tipo == 'vendedor':
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            vendedor_data = VendedorSerializer(user.vendedor).data
            return Response({
                'token': token.key,
                'username': user.username,
                'tipo': user.tipo,
                'dados': vendedor_data
            })
        return Response({'error': 'Credenciais inválidas ou usuário não é vendedor'}, status=status.HTTP_401_UNAUTHORIZED)

class ClienteLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.tipo == 'cliente':
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            cliente_data = ClienteSerializer(user.cliente).data
            return Response({
                'token': token.key,
                'username': user.username,
                'tipo': user.tipo,
                'dados': cliente_data
            })
        return Response({'error': 'Credenciais inválidas ou usuário não é cliente'}, status=status.HTTP_401_UNAUTHORIZED)
