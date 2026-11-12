from django.shortcuts import render
from django.views.generic import ListView
from .models import Producto


# ==========================================
# VISTA BASADA EN FUNCIÓN (FBV) - Ruta: /
# ==========================================
def home(request):
    # Contexto básico para la bienvenida
    contexto = {
        "titulo": "Bienvenido al Catálogo Tecnológico",
        "mensaje": "Explora nuestra selección de productos de tecnología.",
        "total_productos": Producto.objects.count(), # QuerySet #1
    }
    return render(request, "home.html", contexto)


# ==========================================
# VISTA BASADA EN CLASE (CBV) - Ruta: /catalogo/
# ==========================================
class ProductoListView(ListView):
    model = Producto
    template_name = "catalogo.html"
    context_object_name = "productos"  # Así se llamará en el template
    
    def get_queryset(self):
        # QuerySet #2: Filtramos los que tienen stock y ordenamos por precio
        # (Lazy Evaluation: esta consulta NO se ejecuta hasta que el template la use)
        return Producto.objects.filter(stock__gt=0).order_by("precio")

    def get_context_data(self, **kwargs):
        # Añadimos variables extra al contexto de la CBV
        context = super().get_context_data(**kwargs)
        context["titulo_pagina"] = "Catálogo de Productos Disponibles"
        return context