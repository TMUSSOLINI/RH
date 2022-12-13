from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from funcionarios.api.views import FuncionarioViewSet
from hora_extra.api.views import HoraExtraViewSet

router = routers.DefaultRouter()
router.register(r'api/funcionarios', FuncionarioViewSet)
router.register(r'api/banco-horas', HoraExtraViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('funcionarios/', include('funcionarios.urls')),
    path('depatarmentos/', include('departamentos.urls')),
    path('empresas/', include('empresas.urls')),
    path('documentos/', include('documentos.urls')),
    path('hora-extra/', include('hora_extra.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
