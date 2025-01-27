from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'short_content', 'created_at', 'updated_at')  # Mostrar estos campos
    list_display_links = ('updated_at',)  # Enlace clickeable (para evitar conflicto con list_editable)
    list_editable = ('title',)  # Campo editable desde la lista
    search_fields = ('title', 'subtitle', 'content')  # Campos para buscar
    list_filter = ('created_at',)  # Filtros por fecha de creación
    ordering = ('-created_at',)  # Ordenar los más recientes primero
    list_per_page = 20  # Paginación en el admin

    # Método para mostrar una vista previa del contenido
    def short_content(self, obj):
        return obj.content[:50]  # Muestra los primeros 50 caracteres
    short_content.short_description = "Preview"
