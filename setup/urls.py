from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from jornada_milhas.views import DepoimentosViewSet

router = routers.DefaultRouter()
router.register('depoimentos', DepoimentosViewSet, basename='Depoimentos')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
