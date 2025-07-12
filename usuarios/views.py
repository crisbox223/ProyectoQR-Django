# views.py - Versión consolidada
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Usuario  # Importa tu modelo de usuario personalizado
from .decorators import role_required  # Importa el decorador personalizado

# --------------------------
# VISTAS DE AUTENTICACIÓN
# --------------------------

def login_view(request):
    """
    Maneja el inicio de sesión de usuarios y redirección según rol
    """
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            # Redirección basada en roles
            if user.rol == 'estudiante':
                return redirect('vista_estudiante')
            elif user.rol == 'profesor':
                return redirect('vista_profesor')
            elif user.rol == 'mensualidad':
                return redirect('vista_mensualidad')
            elif user.rol == 'empleado':
                return redirect('vista_empleado')
            else:
                return redirect('pagina_principal')
        else:
            return render(request, 'login.html', {
                'error': 'Usuario o contraseña incorrectos'
            })
    
    return render(request, 'login.html')

def logout_view(request):
    """
    Cierra la sesión del usuario
    """
    logout(request)
    return redirect('login') # Aquí estás redirigiendo a 'login', lo cual es correcto.

# --------------------------
# VISTAS PROTEGIDAS POR ROL
# --------------------------

@login_required
@role_required(allowed_roles=['estudiante'])
def vista_estudiante(request):
    """
    Vista exclusiva para estudiantes
    """
    contexto = {
        'usuario': request.user,
        'seccion': 'Estudiante'
    }
    return render(request, 'usuarios/estudiante.html', contexto)

@login_required
@role_required(allowed_roles=['profesor'])
def vista_profesor(request):
    """
    Vista exclusiva para profesores
    """
    contexto = {
        'usuario': request.user,
        'seccion': 'Profesor'
    }
    return render(request, 'usuarios/profesor.html', contexto)
    
    # Puedes agregar aquí más vistas protegidas por rol si lo necesitas
@login_required
@role_required(allowed_roles=['mensualidad'])
def vista_mensualidad(request):
    """
    Vista exclusiva para administración de mensualidades
    """
    contexto = {
        'usuario': request.user,
        'seccion': 'Mensualidad'
    }
    return render(request, 'usuarios/mensualidad.html', contexto)


@login_required
@role_required(allowed_roles=['empleado'])
def vista_empleado(request):
    """
    Vista exclusiva para empleado
    """
    contexto = {
        'usuario': request.user,
        'seccion': 'Empleado'
    }
    return render(request, 'usuarios/empleado.html', contexto)

def pagina_prueba(request):
    return HttpResponse("¡Esta prueba funciona!")
# --------------------------
# VISTAS GENERALES
# --------------------------

@login_required
def pagina_principal(request):
    """
    Vista principal después del login (para roles no especificados)
    """
    return render(request, 'base.html')

def handler403(request, exception=None):
    """
    Maneja errores 403 (acceso prohibido)
    """
    return render(request, '403.html', status=403)

def handler404(request, exception=None):
    """
    Maneja errores 404 (página no encontrada)
    """
    return render(request, '404.html', status=404)