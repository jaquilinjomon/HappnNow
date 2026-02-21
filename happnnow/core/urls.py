from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard_router, name='dashboard'),
    path('reviews/', views.reviews_view, name='reviews'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
