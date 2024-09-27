from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='blog-index'),
    path('create', views.create, name='blog-create'),
    path('edit/<int:pk>', views.edit, name='blog-edit'),
    path('delete/<int:pk>', views.delete, name='blog-delete'),
]