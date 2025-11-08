# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
import re

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = [
            "username", "nombre", "apellido", "rut",
            "direccion", "email", "password1", "password2"
        ]
        labels = {
            "username": "Nombre de usuario",
            "nombre": "Nombre",
            "apellido": "Apellido",
            "rut": "RUT",
            "direccion": "Dirección",
            "email": "Correo electrónico",
            "password1": "Contraseña",
            "password2": "Confirmar contraseña",
        }

    def clean_rut(self):
        rut = self.cleaned_data.get("rut")
        if not re.match(r"^\d{7,8}-[0-9Kk]$", rut):
            raise forms.ValidationError("El RUT debe tener el formato 12345678-9 o 12345678-K.")
        return rut

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if Usuario.objects.filter(email=email).exists():
            raise forms.ValidationError("Ya existe un usuario con ese correo.")
        return email
