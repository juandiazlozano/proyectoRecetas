from django.urls import path
from . import views

app_name = 'recetas'

urlpatterns = [
    path('', views.index, name='index'),
    path('receta/<int:pk>/', views.detalle, name='detalle'),
    path('crear/', views.crear_receta, name='crear'),
    path('recomendador/', views.recomendador, name='recomendador'),  # <-- agregada
]
