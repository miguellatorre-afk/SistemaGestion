from django.contrib import admin
from .models import Cliente, Producto

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dni', 'email') 
    search_fields = ('nombre', 'dni')        

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('sku', 'nombre', 'precio_base')
    search_fields = ('sku', 'nombre')
    list_filter = ('precio_base',)         