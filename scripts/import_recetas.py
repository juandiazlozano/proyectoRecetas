# Script para importar core/ia/artefactos/recetas.csv al modelo Receta
# Ejecutar: python scripts/import_recetas.py
import os, sys, csv
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

import django
django.setup()
from recetas.models import Receta

csv_path = os.path.join(BASE, 'core', 'ia', 'artefactos', 'recetas.csv')
if not os.path.exists(csv_path):
    print('No se encontró', csv_path)
    sys.exit(1)

with open(csv_path, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    contador = 0
    for row in reader:
        Receta.objects.create(
            nombre=row.get('nombre') or 'Sin nombre',
            categoria=row.get('categoria') or '',
            origen=row.get('origen') or '',
            ingredientes=row.get('ingredientes') or '',
            descripcion=row.get('descripcion') or '',
            tiempo_preparacion=int(row.get('tiempo_preparacion') or 0),
            dificultad=row.get('dificultad') or 'fácil'
        )
        contador += 1
print(f'Importadas {contador} recetas')
