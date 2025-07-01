from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    TIPOS = (
        ('admin', 'Administrador'),
        ('vendedor', 'Vendedor'),
        ('cliente', 'Cliente'),
    )
    tipo = models.CharField(max_length=10, choices=TIPOS)

class Administrador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='administrador')
    # campos extras do administrador (se precisar)

class Vendedor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='vendedor')
    # exemplo: código do vendedor
    codigo = models.CharField(max_length=20, unique=True)

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')
    cpf = models.CharField(max_length=14, unique=True)
    # outros dados do cliente
