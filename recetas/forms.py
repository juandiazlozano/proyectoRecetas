from django import forms
from .models import Receta

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = '__all__'

        widgets = {
            "nombre": forms.TextInput(attrs={
                "placeholder": "Ej: Sopa de pollo"
            }),
            "categoria": forms.TextInput(attrs={
                "placeholder": "Ej: Almuerzo, Postre..."
            }),
            "origen": forms.TextInput(attrs={
                "placeholder": "Ej: Colombia"
            }),
            "ingredientes": forms.Textarea(attrs={
                "rows": 4,
                "placeholder": "Ej: arroz, pollo, cebolla, sal"
            }),
            "descripcion": forms.Textarea(attrs={
                "rows": 5,
                "placeholder": "Describe cómo preparar la receta"
            }),
            "tiempo_preparacion": forms.NumberInput(attrs={
                "min": 1
            }),
            "dificultad": forms.Select()
        }
