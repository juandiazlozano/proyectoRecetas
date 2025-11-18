from django.contrib import admin
from .models import Receta

@admin.register(Receta)
class RecetaAdmin(admin.ModelAdmin):
    list_display = ('nombre','categoria','origen','tiempo_preparacion','dificultad')
    search_fields = ('nombre','ingredientes','origen','categoria')
