from django.shortcuts import render
from .forms import SuperAdministradorEquipos, SuperAdministradorUsuarios, SuperAdministradorMantenimientos, AdministradorVentana, AdministradorVentanaUsuarios, AdministradorVentanaManatenimientos
from .models import DatosUsuario, DatosEquipo, Mantenimientos_equipos

# Create your views here.
def home(request):      
        

    return render(request, "home.html", {})


def datosusuarios(request):
    form = SuperAdministradorUsuarios(request.POST or None)
    if form.is_valid(): 
        instance = form.save(commit=False)
        Usuario = form.cleaned_data.get("Usuario")
        departamento = form.cleaned_data.get("departamento")
        instance.save()
        instance.clean()

    context = {

        "el_form": form, 
    }

    if request.user.is_authenticated and request.user.is_staff:
        queryset = DatosUsuario.objects.all().order_by("Usuario")
       

        context = {

            "queryset": queryset,
        }

    
    return render(request, "usuario.html", context)



def datos_equipo(request):
    form = SuperAdministradorEquipos(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        Nombre_PC = form.cleaned_data.get("Nombre_PC")
        Tipo = form.cleaned_data.get("Tipo")
        Marca = form.cleaned_data.get("Marca")
        Modelo = form.cleaned_data.get("Modelo")
        Usuario = form.cleaned_data.get("Usuario")
        instance.save()

        


    context = {

        "el_form": form,
    }


    if request.user.is_authenticated and request.user.is_staff:
        queryset = DatosEquipo.objects.all().order_by("Nombre_PC")
       

        context = {

            "queryset": queryset,
        }

    
    return render(request, "equipo.html", context)
        

def datos_mantenimiento(request):
    form = SuperAdministradorMantenimientos(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        Fecha = form.cleaned_data.get("Fecha")
        Observaciones = form.cleaned_data.get("Observaciones")
        Datos_equipo = form.cleaned_data.get("Datos_equipo")
        instance.save()
        

    context = {

        "el_form": form,
    }

    if request.user.is_authenticated and request.user.is_staff:
        queryset = Mantenimientos_equipos.objects.all().order_by("Fecha")
       

        context = {

            "queryset": queryset,
        }
    
    return render(request, "mantenimiento.html", context)


    
    