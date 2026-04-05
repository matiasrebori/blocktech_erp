from django.db import models


class GastoGeneral(models.Model):

    CATEGORIAS = [
        ("alquiler", "Alquiler"),
        ("servicios", "Servicios"),
        ("sueldos", "Sueldos"),
        ("software", "Software"),
        ("marketing", "Marketing"),
        ("otros", "Otros"),
    ]

    concepto = models.CharField(max_length=255)
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)

    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateField()

    descripcion = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.concepto} - {self.monto}"