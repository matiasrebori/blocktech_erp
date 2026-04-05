from django.contrib import admin
from .models import Pago


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ("proyecto", "monto", "tipo", "fecha")
    list_filter = ("tipo", "fecha")
    search_fields = ("proyecto__nombre",)