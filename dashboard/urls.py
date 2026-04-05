from django.urls import path
from .views import dashboard_view, proyecto_detalle_view

urlpatterns = [
    path("", dashboard_view, name="dashboard"),
    path("proyecto/<int:proyecto_id>/", proyecto_detalle_view, name="proyecto_detalle"),
]