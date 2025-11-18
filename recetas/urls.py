from django.urls import path
from . import views

app_name = 'recetas'

urlpatterns = [
    path('', views.index, name='index'),
    path('receta/<int:pk>/', views.detalle, name='detalle'),
    path('crear/', views.crear, name='crear'),
    path('eliminar/<int:pk>/', views.eliminar_receta, name='eliminar'),
    path('recomendador/', views.recomendador, name='recomendador'),
]
