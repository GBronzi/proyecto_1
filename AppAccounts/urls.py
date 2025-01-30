from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views
from .views import edit_profile

app_name = 'AppAccounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.signup_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('edit-profile/', views.edit_profile_view, name='edit_profile'),
    path('change-password/', views.CustomPasswordChangeView.as_view(), name='change_password'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('edit-profile/', edit_profile, name="edit_profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
