from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('depatarmentos/', include('departamentos.urls')),
    path('empresas/', include('empresas.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
