#transcript_app/urls.py
from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('transcript/', views.transcript, name='transcript'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
