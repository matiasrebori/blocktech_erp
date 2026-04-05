from django.contrib import admin
from .models import Compra, DetalleCompra, Proveedor


class DetalleCompraInline(admin.TabularInline):
    model = DetalleCompra
    extra = 1  # cantidad de filas vacías iniciales


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "proyecto", "proveedor", "fecha")
    list_filter = ("proveedor", "fecha")
    search_fields = ("proveedor__nombre", "proyecto__nombre")
    autocomplete_fields = ("proveedor", "proyecto")
    inlines = [DetalleCompraInline]


@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    search_fields = ("nombre",)