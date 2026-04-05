from django.db import models

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    cliente = models.CharField(max_length=200)
    presupuesto_total = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=50, default="pendiente")

    def __str__(self):
        return self.nombre
    
    @property
    def total_costos(self):
        from compras.models import Compra
        return sum(
            sum(d.subtotal() for d in compra.detalles.all())
            for compra in self.compra_set.all()
        )

    @property
    def total_ingresos(self):
        from pagos.models import Pago
        return sum(p.monto for p in self.pago_set.all())

    @property
    def profit(self):
        return self.total_ingresos - self.total_costos