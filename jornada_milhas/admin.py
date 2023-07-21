from django.contrib import admin
from jornada_milhas.models import Depoimento

class Depoimentos(admin.ModelAdmin):
    list_display = ('id','foto','nome','depoimento')
    list_display_links = ('id','nome')
    search_fields = ('nome',)
    list_per_page = 20

admin.site.register(Depoimento,Depoimentos)