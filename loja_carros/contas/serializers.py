from rest_framework import serializers
from .models import User, Administrador, Vendedor, Cliente

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'tipo', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class AdministradorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Administrador
        fields = ['user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['tipo'] = 'admin'
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        administrador = Administrador.objects.create(user=user, **validated_data)
        return administrador

class VendedorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Vendedor
        fields = ['codigo', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['tipo'] = 'vendedor'
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        vendedor = Vendedor.objects.create(user=user, **validated_data)
        return vendedor

class ClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Cliente
        fields = ['cpf', 'user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['tipo'] = 'cliente'
        user_serializer = UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()
        cliente = Cliente.objects.create(user=user, **validated_data)
        return cliente
