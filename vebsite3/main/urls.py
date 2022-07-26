from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='home'),
    path('gggg', views.about, name='about'),
    path('storm/', views.storm),
    path('create', views.about, name='create'),
]
