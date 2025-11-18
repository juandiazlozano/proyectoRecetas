from django.db import models
from django.core.exceptions import ValidationError

class Receta(models.Model):

    CATEGORIAS = [
        ('sopa', 'Sopa'),
        ('carne', 'Carne'),
        ('ensalada', 'Ensalada'),
        ('postre', 'Postre'),
        ('bebida', 'Bebida'),
        ('otros', 'Otros'),
    ]

    DIFICULTADES = [
        ('fácil', 'Fácil'),
        ('media', 'Media'),
        ('difícil', 'Difícil'),
    ]

    nombre = models.CharField(max_length=200)

    # Ahora es un choice (mejor presentación, más profesional)
    categoria = models.CharField(
        max_length=50, 
        choices=CATEGORIAS,
        default='otros'
    )

    origen = models.CharField(max_length=100, blank=True, null=True)

    ingredientes = models.TextField(
        help_text='Lista de ingredientes separados por coma'
    )

    descripcion = models.TextField(blank=True, null=True)

    tiempo_preparacion = models.IntegerField(
        help_text='Tiempo en minutos',
        default=0
    )

    dificultad = models.CharField(
        max_length=20,
        choices=DIFICULTADES,
        default='fácil'
    )

    creado_en = models.DateTimeField(auto_now_add=True)

    # -------- Validación opcional pero útil --------
    def clean(self):
        if not self.ingredientes.strip():
            raise ValidationError("La receta debe tener al menos un ingrediente.")

    # -------- Representación bonita --------
    def __str__(self):
        return f"{self.nombre} — {self.categoria}"

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"
