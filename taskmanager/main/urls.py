from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='home'),
    path('about/<str:criteria>/', views.about, name='about'),
    path('film/<int:article_id>/', views.film, name='film'),
    path('create', views.create, name='create'),
]
