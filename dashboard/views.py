from django.shortcuts import render, get_object_or_404
from django.db.models import Sum
from datetime import datetime

from proyectos.models import Proyecto
from pagos.models import Pago
from compras.models import Compra
from core.models import GastoGeneral


def dashboard_view(request):
    anio = int(request.GET.get("anio", datetime.now().year))

    # Ingresos (pagos)
    ingresos = Pago.objects.filter(fecha__year=anio).aggregate(
        total=Sum("monto")
    )["total"] or 0

    # Costos (compras)
    costos = 0
    compras = Compra.objects.filter(fecha__year=anio)

    for compra in compras:
        for d in compra.detalles.all():
            costos += d.subtotal()

    # gastos inherentes
    gastos = GastoGeneral.objects.filter(fecha__year=anio).aggregate(
        total=Sum("monto")
    )["total"] or 0

    resultado = ingresos - costos - gastos

    # Proyectos con métricas
    proyectos_data = []

    proyectos = Proyecto.objects.all()

    for p in proyectos:
        proyectos_data.append({
            "id": p.id,
            "nombre": p.nombre,
            "ingresos": p.total_ingresos,
            "costos": p.total_costos,
            "profit": p.profit,
        })

    context = {
        "anio": anio,
        "total_ingresos": ingresos,
        "total_costos": costos,
        "total_gastos": gastos,
        "resultado": resultado,
        "proyectos": proyectos_data,
    }

    return render(request, "dashboard/dashboard.html", context)

def proyecto_detalle_view(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)

    pagos = proyecto.pago_set.all()
    compras = proyecto.compra_set.all()

    context = {
        "proyecto": proyecto,
        "pagos": pagos,
        "compras": compras,
    }

    return render(request, "dashboard/proyecto_detalle.html", context)