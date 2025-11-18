import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

class RecipeRecommender:

    def __init__(self, vectorizer, matrix, recipes):
        self.vectorizer = vectorizer
        self.matrix = matrix
        self.recipes = recipes

    def recommend(self, ingredients_text, top=5):
        user_vec = self.vectorizer.transform([ingredients_text])
        similarities = cosine_similarity(user_vec, self.matrix).flatten()
        indices = similarities.argsort()[::-1][:top]
        return [(self.recipes[i], similarities[i]) for i in indices]
