from django.contrib import admin
from .models import GastoGeneral


@admin.register(GastoGeneral)
class GastoGeneralAdmin(admin.ModelAdmin):

    list_display = (
        "concepto",
        "categoria",
        "monto",
        "fecha",
    )

    list_filter = (
        "categoria",
        "fecha",
    )

    search_fields = (
        "concepto",
        "descripcion",
    )

    ordering = ("-fecha",)

    date_hierarchy = "fecha"