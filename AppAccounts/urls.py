from django.urls import path
from . import views

app_name = 'AppAccounts'

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.signup_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('edit-profile/', views.edit_profile_view, name='edit_profile'),
    path('change-password/', views.CustomPasswordChangeView.as_view(), name='change_password'),
]
