from django.contrib import admin
from .models import Pedido, LineaPedido

class LineaPedidoInline(admin.TabularInline):
    model = LineaPedido
    extra = 1 # Número de líneas vacías que aparecen por defecto

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'fecha', 'estado') # Lo que ves en la tabla
    list_filter = ('estado', 'fecha')                  # Filtros rápidos
    search_fields = ('cliente__nombre',)               # Buscar por nombre de cliente
    inlines = [LineaPedidoInline]                      # Insertar las líneas dentro