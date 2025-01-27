from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

app_name = 'AppBlog'

urlpatterns = [
    path('', PostListView.as_view(), name='list'),  # Listado de posts
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),  # Detalle de un post
    path('create/', PostCreateView.as_view(), name='create'),  # Crear un post
    path('update/<int:pk>/', PostUpdateView.as_view(), name='update'),  # Editar un post
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='delete'),  # Borrar un post
]
