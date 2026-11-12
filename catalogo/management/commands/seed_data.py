from django.core.management.base import BaseCommand
from catalogo.models import Producto

class Command(BaseCommand):
    help = 'Pobla la base de datos con productos de prueba'

    def handle(self, *args, **kwargs):
        # Limpiamos la tabla para no duplicar si lo corremos varias veces
        Producto.objects.all().delete()
        
        productos = [
            {"nombre": "Laptop Gamer ASUS ROG", "precio": 4500.00, "categoria": "Laptops", "stock": 10},
            {"nombre": "Mouse Logitech G502", "precio": 150.50, "categoria": "Periféricos", "stock": 3}, # Stock bajo
            {"nombre": "Teclado Mecánico Redragon", "precio": 200.00, "categoria": "Periféricos", "stock": 0}, # Agotado
            {"nombre": "Monitor Samsung 24\"", "precio": 800.00, "categoria": "Monitores", "stock": 15},
            {"nombre": "Disco SSD Kingston 1TB", "precio": 350.00, "categoria": "Almacenamiento", "stock": 2}, # Stock bajo
            {"nombre": "Audífonos HyperX Cloud II", "precio": 320.00, "categoria": "Audio", "stock": 8},
            {"nombre": "Procesador Ryzen 7", "precio": 1200.00, "categoria": "Componentes", "stock": 0}, # Agotado
        ]

        for p in productos:
            Producto.objects.create(**p)

        self.stdout.write(self.style.SUCCESS(f'¡Éxito! Se cargaron {len(productos)} productos.'))