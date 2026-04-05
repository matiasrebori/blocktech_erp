from django.db import models
from proyectos.models import Proyecto

class Pago(models.Model):
    TIPO_CHOICES = [
        ("anticipo", "Anticipo"),
        ("saldo", "Saldo"),
    ]

    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha = models.DateField(auto_now_add=True)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return f"{self.proyecto} - {self.monto}"