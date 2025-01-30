from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages  
from .models import Post
from .forms import PostForm

# =============================Listar y ver post================================================
class PostListView(ListView):
    model = Post  
    template_name = 'AppBlog/list.html'  
    context_object_name = 'posts'  
    ordering = ['-created_at']  


class PostDetailView(DetailView):
    model = Post
    template_name = 'AppBlog/detail.html'

# =============================Crear post================================================
class PostCreateView(CreateView):
    model = Post
    form_class = PostForm  
    template_name = 'AppBlog/form.html'

    def form_valid(self, form):
        """
        Se ejecuta cuando el formulario es válido.
        Guarda el post y muestra un mensaje de éxito.
        """
        response = super().form_valid(form)
        messages.success(self.request, '¡Post creado exitosamente!')  # Notificación de éxito
        return response

    success_url = reverse_lazy('AppBlog:list') 

# =============================Actualizar post================================================
class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm  
    template_name = 'AppBlog/form.html'

    def form_valid(self, form):
        """
        Se ejecuta cuando el formulario es válido.
        Guarda los cambios y muestra un mensaje de éxito.
        """
        response = super().form_valid(form)
        messages.success(self.request, '¡Post actualizado exitosamente!')  # Notificación de éxito
        return response

    success_url = reverse_lazy('AppBlog:list')  

# =============================Eliminar post================================================
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'AppBlog/delete.html'  

    def delete(self, request, *args, **kwargs):
        """
        Se ejecuta cuando se elimina un post.
        Borra el post y muestra un mensaje de éxito.
        """
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, '¡Post eliminado exitosamente!')  # Notificación de éxito
        return response

    success_url = reverse_lazy('AppBlog:list')  
