# Importamos HttpResponseForbidden para devolver una respuesta HTTP 403 (Prohibido)
from django.http import HttpResponseForbidden

# Definimos un decorador que verifica los roles de usuario
def role_required(allowed_roles=[]):
    """
    Decorador que restringe el acceso a una vista basado en los roles del usuario.
    
    Parámetros:
        allowed_roles (list): Lista de roles permitidos para acceder a la vista
    """
    
    # Decorador interno que recibe la función de vista (view function)
    def decorator(view_func):
        # Vista envuelta que realiza la verificación de roles
        def _wrapped_view(request, *args, **kwargs):
            """
            Verifica si el usuario tiene el rol requerido antes de ejecutar la vista.
            
            Retorna:
                - La vista original si el usuario está autenticado y tiene el rol adecuado
                - HttpResponseForbidden (403) si no cumple los requisitos
            """
            
            # Verifica: 1) que el usuario esté autenticado y 2) que su rol esté en los permitidos
            if request.user.is_authenticated and request.user.rol in allowed_roles:
                # Si cumple, ejecuta la vista original
                return view_func(request, *args, **kwargs)
            
            # Si no cumple los requisitos, retorna error 403 (Prohibido)
            return HttpResponseForbidden("No tienes permiso para ver esta página.")
        
        return _wrapped_view
    
    return decorator