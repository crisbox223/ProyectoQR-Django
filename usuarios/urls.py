# tu_proyecto/urls.py (por ejemplo, parqueadero/urls.py según tu imagen)
from django.contrib import admin
from django.urls import path, include
from usuarios import views # Asume que tus vistas de autenticación están en la app 'usuarios'

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # 1. Incluye las URLs de autenticación de Django.
    #    Esto automáticamente proporciona URLs con nombres como 'login', 'logout', etc.
    #    La vista 'logout' de Django.contrib.auth.views.logout_view ya está mapeada aquí con name='logout'.
    #    Si quieres usar tu propia logout_view, no necesitas esta línea para 'logout',
    #    pero aun así es útil para otras funcionalidades de auth.
    path('accounts/', include('django.contrib.auth.urls')),
    
    # 2. Mapea tu propia vista de login.
    #    Es común tener un 'login' personalizado, por lo que lo mapeas directamente.
    path('login/', views.login_view, name='login'),
    
    # 3. Mapea tu propia vista de logout si no estás usando la de Django y quieres una URL específica.
    #    Dado que tienes tu propia logout_view en views.py, es buena idea mapearla.
    path('logout/', views.logout_view, name='logout'), # <--- ESTA LÍNEA ES CLAVE
    
    # Rutas para tus vistas protegidas por rol
    path('estudiante/', views.vista_estudiante, name='vista_estudiante'),
    path('profesor/', views.vista_profesor, name='vista_profesor'),
    path('mensualidad/', views.vista_mensualidad, name='vista_mensualidad'),
    path('empleado/', views.vista_empleado, name='vista_empleado'),

    # Otras rutas generales
    path('pagina_principal/', views.pagina_principal, name='pagina_principal'),
    path('pagina_prueba/', views.pagina_prueba, name='pagina_prueba')
    # ... otras URLs de tus aplicaciones
]

# También necesitas definir los manejadores de errores en tu urls.py principal
handler403 = 'usuarios.views.handler403' # Asumiendo que handler403 está en views de la app 'usuarios'
handler404 = 'usuarios.views.handler404' # Asumiendo que handler404 está en views de la app 'usuarios'