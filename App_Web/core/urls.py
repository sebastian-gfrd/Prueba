from django.urls import path

from .api_views import (
    PerformancePublicStatsView,
    RecursosInfrautilizadosView,
    SolicitudReporteListCreateView,
)
from .views import health

urlpatterns = [
    path("health/", health, name="health"),
    path(
        "api/v1/public/performance-stats/",
        PerformancePublicStatsView.as_view(),
        name="api-public-performance-stats",
    ),
    path(
        "api/v1/reportes/mensuales/",
        SolicitudReporteListCreateView.as_view(),
        name="api-reportes-mensuales",
    ),
    path(
        "api/v1/analisis/recursos-infrautilizados/",
        RecursosInfrautilizadosView.as_view(),
        name="api-recursos-infrautilizados",
    ),
]
