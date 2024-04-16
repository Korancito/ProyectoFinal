from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# -------------- Proveedores 


class Proveedor(models.Model):
    
    razonsocial = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60) 
    rut = models.IntegerField()
    giro = models.CharField(max_length=60)
    
    def __str__(self):
        return f"{self.razonsocial} {self.nombre} {self.rut} {self.giro}"

# ------------- Categoria

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    
    
    objects = models.Manager()
    
    
    def __str__(self):
        return self.nombre
    
   
    
# ------------ Productos 


class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    cantidad = models.IntegerField(null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    precio_costo = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE )
    
    
    
    def __str__(self):
        return f"{self.nombre}, {self.cantidad}, {self.precio}, {self.precio_costo}, {self.categoria}"


# ------------- Staff


class Staff(models.Model):
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    
    def __str__(self):
        return self.nombre, self.apellido, self.status, self.contacto, self.email
    
