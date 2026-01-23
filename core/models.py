from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=255)
    dni = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.nombre} - {self.email}"

class Producto(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    nombre = models.CharField(max_length=255)
    precio_base = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.sku} - {self.nombre}"