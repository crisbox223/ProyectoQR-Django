# Importamos las clases necesarias de Django
from django.contrib.auth.models import AbstractUser  # Clase abstracta base para usuarios
from django.db import models  # Módulo para definir modelos de base de datos

# Definimos nuestro modelo de Usuario personalizado heredando de AbstractUser
class Usuario(AbstractUser):
    """
    Modelo de usuario personalizado que extiende el modelo AbstractUser de Django.
    Añade un campo 'rol' para manejar diferentes tipos de usuarios en el sistema.
    """
    
    # Definición de posibles roles para los usuarios
    ROL_CHOICES = [
        ('estudiante', 'Estudiante'),       # Opción para estudiantes
        ('profesor', 'Profesor'),   
        ('empleado', 'Empleado'),        # Opción para empleados
        ('mensualidad', 'Mensualidad'),     # Opción para gestión de mensualidades
    ]
    
    # Campo para almacenar el rol del usuario
    rol = models.CharField(
        max_length=20,           # Longitud máxima del campo
        choices=ROL_CHOICES,     # Opciones disponibles para este campo
        default='estudiante'     # Valor por defecto si no se especifica
    )