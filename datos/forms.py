from django import forms
from .models import DatosUsuario, DatosEquipo, Mantenimientos_equipos



class SuperAdministradorUsuarios(forms.ModelForm):
    class Meta:
        model = DatosUsuario
        fields = '__all__'

class SuperAdministradorEquipos(forms.ModelForm):
    class Meta:
        model = DatosEquipo
        fields = '__all__'

        
class SuperAdministradorMantenimientos(forms.ModelForm):
    class Meta:
        model = Mantenimientos_equipos
        fields = '__all__'


class AdministradorVentana(forms.Form):
    Nombre_PC = forms.CharField(max_length=30)
    Tipo = forms.CharField(max_length=30)
    Marca = forms.CharField(max_length=30)
    Modelo = forms.CharField(max_length=30)
    Usuario = forms.CharField(max_length=30)
    

class AdministradorVentanaUsuarios(forms.Form):
    Usuario = forms.CharField(max_length=30)
    departamento = forms.CharField(max_length=15)

class AdministradorVentanaManatenimientos(forms.Form):
    Fecha = forms.DateField()
    Observaciones = forms.CharField(min_length=30)
    Datos_equipo = forms.CharField(max_length=30)


