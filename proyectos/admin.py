from django.contrib import admin
from .models import Proyecto


@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "cliente", "presupuesto_total", "estado", "fecha_inicio", "fecha_fin")
    search_fields = ("nombre", "cliente")
    list_filter = ("estado", "fecha_inicio")