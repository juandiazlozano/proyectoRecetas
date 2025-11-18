from django.shortcuts import render, get_object_or_404, redirect
from .models import Receta
from .forms import RecetaForm
import pickle
import os
import numpy as np

def index(request):
    recetas = Receta.objects.all()[:50]
    return render(request, 'recetas/index.html', {'recetas': recetas})

def detalle(request, pk):
    receta = get_object_or_404(Receta, pk=pk)
    return render(request, 'recetas/detalle.html', {'receta': receta})

def crear_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recetas:index')
    else:
        form = RecetaForm()
    return render(request, 'recetas/crear.html', {'form': form})

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def recomendador(request):
    resultados = []
    ingredientes_usuario = ""
    lista_ing = []

    if request.method == "POST":
        ingredientes_usuario = request.POST.get("ingredientes", "")
        lista_ing = [i.strip().lower() for i in ingredientes_usuario.split(",") if i.strip()]

        # Cargar modelo entrenado
        modelo_path = os.path.join(BASE_DIR, "scripts", "modelo_recetas.pkl")
        with open(modelo_path, "rb") as f:
            modelo = pickle.load(f)

        # Pedir recomendaciones
        resultados_df = modelo.recomendar(lista_ing)

        # Calcular coincidencias
        def contar_coincidencias(ingredientes_receta):
            receta_set = set([i.strip().lower() for i in ingredientes_receta.split(",")])
            return len(receta_set.intersection(lista_ing))

        resultados_df["coincidencias"] = resultados_df["ingredientes"].apply(contar_coincidencias)
        resultados_df = resultados_df.sort_values(by="coincidencias", ascending=False)

        # **Limitar a las 15 mejores recetas**
        resultados_df = resultados_df.head(15)

        # Convertir a lista de diccionarios
        resultados = resultados_df.to_dict(orient="records")

        # Agregar lista de ingredientes ya separados a cada receta
        for receta in resultados:
            receta["ingredientes_lista"] = [i.strip() for i in receta["ingredientes"].split(",")]

    return render(
        request,
        "recetas/recomendador.html",
        {
            "resultados": resultados,
            "ingredientes": lista_ing
        }
    )
