from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages  # Importar los mensajes
from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'AppBlog/list.html'
    context_object_name = 'posts'
    ordering = ['-created_at']

class PostDetailView(DetailView):
    model = Post
    template_name = 'AppBlog/detail.html'

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'AppBlog/form.html'
    
    def form_valid(self, form):
        # Guarda el formulario
        response = super().form_valid(form)
        
        # Añade un mensaje de éxito después de la creación
        messages.success(self.request, '¡Post creado exitosamente!')
        return response

    success_url = reverse_lazy('AppBlog:list')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'AppBlog/form.html'

    def form_valid(self, form):
        # Guarda el formulario
        response = super().form_valid(form)
        
        # Añade un mensaje de éxito después de la actualización
        messages.success(self.request, '¡Post actualizado exitosamente!')
        return response

    success_url = reverse_lazy('AppBlog:list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'AppBlog/delete.html'

    def delete(self, request, *args, **kwargs):
        # Realiza la eliminación
        response = super().delete(request, *args, **kwargs)
        
        # Añade un mensaje de éxito después de la eliminación
        messages.success(self.request, '¡Post eliminado exitosamente!')
        return response

    success_url = reverse_lazy('AppBlog:list')
