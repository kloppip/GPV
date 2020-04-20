from django.db import models

# Create your models here.
class DatosUsuario(models.Model):
    Usuario = models.CharField(max_length=30, null=True)
    departamento = models.CharField(max_length=15, null=True)
    
    def __str__(self):
        cadena = "{0} {1}"
        return cadena.format(self.Usuario, self.departamento)

class DatosEquipo(models.Model):
    Nombre_PC = models.CharField(max_length=30)
    Tipo = models.CharField(max_length=30, null=True)
    Marca = models.CharField(max_length=30, null=True)
    Modelo = models.CharField(max_length=30, null=True)
    Usuario = models.ForeignKey(DatosUsuario, on_delete=models.CASCADE)

    def __str__(self):
        cedena = "{0} {1} {2} {3} {4}"
        return cedena.format(self.Nombre_PC, self.Tipo, self.Marca, self.Modelo, self.Usuario)


class Mantenimientos_equipos(models.Model):
    Fecha = models.DateField()
    Observaciones = models.TextField("Observaciones", blank=True)
    Datos_equipo = models.ForeignKey(DatosEquipo, on_delete=models.CASCADE)

    def __str__(self):
        cadena = "{0} {1} {2}"
        return cadena.format(self.Fecha, self.Observaciones, self.Datos_equipo)