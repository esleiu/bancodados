from django.urls import path
from .views import (
    AdministradorRegistrationView, VendedorRegistrationView, ClienteRegistrationView,
    AdministradorLoginView, VendedorLoginView, ClienteLoginView
)

urlpatterns = [
    path('api/auth/registro/admin/', AdministradorRegistrationView.as_view(), name='registro-admin'),
    path('api/auth/registro/vendedor/', VendedorRegistrationView.as_view(), name='registro-vendedor'),
    path('api/auth/registro/cliente/', ClienteRegistrationView.as_view(), name='registro-cliente'),

    path('api/auth/login/admin/', AdministradorLoginView.as_view(), name='login-admin'),
    path('api/auth/login/vendedor/', VendedorLoginView.as_view(), name='login-vendedor'),
    path('api/auth/login/cliente/', ClienteLoginView.as_view(), name='login-cliente'),
]
