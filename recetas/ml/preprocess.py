from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer

def build_vectorizer(recipes_text): # se construye el vectorizador TF-IDF y la matriz vectorizada/ recipes_text = lista con los ingredientes de cada receta.


    vectorizer = TfidfVectorizer(stop_words="spanish")
    matrix = vectorizer.fit_transform(recipes_text)

    return vectorizer, matrix
