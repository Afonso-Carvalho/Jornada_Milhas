from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from jornada_milhas.views import DepoimentosViewSet, DepoimentosHomeViewSet,DestinosViewSet
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register('depoimentos', DepoimentosViewSet, basename='Depoimentos')
router.register('depoimentos-home', DepoimentosHomeViewSet, basename='Depoimentos-home')
router.register('destinos',DestinosViewSet,basename='Destinos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
