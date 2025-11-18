import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # Agrega la carpeta raíz al path

import pandas as pd
import pickle
from recetas.recomendador_model import RecomendadorRecetas

# Ruta del CSV
df_path = os.path.join(os.path.dirname(__file__), "recetas.csv")
df = pd.read_csv(df_path)

# Entrenar modelo
modelo = RecomendadorRecetas(df)

# Guardar modelo entrenado
with open("modelo_recetas.pkl", "wb") as f:
    pickle.dump(modelo, f)

print("Modelo entrenado y guardado correctamente")
