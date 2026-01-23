from django.db import models
from django.db.models import CheckConstraint, Q
from core.models import Cliente, Producto 

class Pedido(models.Model):
    ESTADOS = [
        ('BORRADOR', 'Borrador'),
        ('CONFIRMADO', 'Confirmado'),
        ('TALLER', 'En Taller'),
        ('FACTURADO', 'Facturado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='BORRADOR')

    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.nombre}"

class LineaPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='lineas', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.PROTECT)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

