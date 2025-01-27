from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
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
    success_url = reverse_lazy('AppBlog:list')

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'AppBlog/form.html'
    success_url = reverse_lazy('AppBlog:list')

class PostDeleteView(DeleteView):
    model = Post
    template_name = 'AppBlog/delete.html'
    success_url = reverse_lazy('AppBlog:list')
