from django.db import models


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.CharField(max_length=50)
    stock = models.PositiveIntegerField()
    creado_en = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["-creado_en"]

    def __str__(self):
        return f"{self.nombre} ({self.categoria})"

    @property
    def disponible(self):
        """True si hay stock. Útil en templates."""
        return self.stock > 0