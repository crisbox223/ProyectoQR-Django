from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario

class UsuarioAdmin(UserAdmin):
    # Muestra el campo 'rol' al crear un usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'rol'),
        }),
    )

    # Muestra el campo 'rol' al editar un usuario
    fieldsets = UserAdmin.fieldsets + (
        ('Rol', {'fields': ('rol',)}),
    )

    list_display = ('username', 'email', 'rol', 'is_staff')
    list_filter = ('rol',)

admin.site.register(Usuario, UsuarioAdmin)
