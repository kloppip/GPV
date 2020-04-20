from django.contrib import admin
from .models import DatosUsuario, DatosEquipo, Mantenimientos_equipos
from .forms import SuperAdministradorUsuarios, SuperAdministradorEquipos, SuperAdministradorMantenimientos
# Register your models here.

class AdministradorUsuarios(admin.ModelAdmin):
    listdisplay = ["Usuario", "departamento"]
    form = SuperAdministradorUsuarios
    search_display = ["Usuario", "departamento"]

    #class Meta:
        #model = DatosUsuario


class AdministradorEquipos(admin.ModelAdmin):
    listdisplay = ["Nombre_PC", "Tipo", "Marca", "Modelo", "Usuario"]
    search_display = ["Nombre_PC", "Usuario"]
    form = SuperAdministradorEquipos
    #class Meta:
        #model = DatosEquipo


class AdministradorMantenimientos(admin.ModelAdmin):
    listdisplay = ["Fecha", "Observaciones", "Datos_equipo"]
    search_display = ["Datos_equipo"]
    form = SuperAdministradorMantenimientos
    #class Meta:
        #model = Mantenimientos


admin.site.register(DatosUsuario, AdministradorUsuarios)
admin.site.register(DatosEquipo, AdministradorEquipos)
admin.site.register(Mantenimientos_equipos, AdministradorMantenimientos)


