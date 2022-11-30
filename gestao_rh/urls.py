from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('depatarmentos/', include('departamentos.urls')),
    path('empresas/', include('empresas.urls')),
    path('documentos/', include('documentos.urls')),
    path('hora-extra/', include('hora_extra.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
