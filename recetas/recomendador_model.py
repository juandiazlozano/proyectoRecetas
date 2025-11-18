import pandas as pd

class RecomendadorRecetas:
    def __init__(self, df):
        """
        Recibe el DataFrame de recetas al inicializar.
        """
        self.df = df

    def recomendar(self, lista_ingredientes):
        """
        Recibe una lista de palabras clave y devuelve todas las recetas que contengan
        al menos uno de esos ingredientes en la columna 'ingredientes'.
        """
        if not lista_ingredientes:
            return pd.DataFrame()  # retorna vacío si no hay ingredientes

        # Convertir columna a minúsculas
        df = self.df.copy()
        df['ingredientes_lower'] = df['ingredientes'].str.lower()

        # Filtrar por cualquier ingrediente de la lista
        mask = df['ingredientes_lower'].apply(lambda x: any(ing in x for ing in lista_ingredientes))
        return df.loc[mask, ['nombre', 'categoria', 'origen', 'ingredientes', 'descripcion']]
