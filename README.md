# Catálogo de Productos Tecnológicos - UNCP

**Asignatura:** Desarrollo de Aplicaciones Web (IS093A)  
**Unidad:** Unidad II: Desarrollo Web Fullstack  
**Tema:** Lenguaje Python: Sintaxis, Estructuras de Control, POO, Excepciones y Módulos (Django MTV)  
**Estudiante:** Andre Pariona Larrota
**Contacto:** andrepariona76@gmail.com  
**Fecha:** 12.11.2026  

---

## 🚀 Descripción del Proyecto
Este proyecto es un Catálogo de Productos Tecnológicos desarrollado con Django, aplicando la arquitectura **MTV (Model-Template-View)**. Incluye una página de bienvenida (FBV) y un catálogo dinámico (CBV) que consume datos reales desde una base de datos SQLite utilizando el ORM de Django.

## 📁 Estructura de Carpetas
```text
catalogo_uncp/
├── config/              # Proyecto principal (settings, urls base)
├── catalogo/            # App de negocio (modelos, vistas, urls)
│   ├── management/      # Comandos personalizados (seed_data)
│   ├── migrations/
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── templates/           # Plantillas HTML globales
│   ├── base.html        # Plantilla maestra (herencia)
│   ├── home.html        # Vista FBV
│   └── catalogo.html    # Vista CBV
├── static/              # Archivos estáticos (CSS)
├── manage.py
├── requirements.txt
└── README.md