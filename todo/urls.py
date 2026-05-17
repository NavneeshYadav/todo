from django.urls import path, include
from . import views
urlpatterns = [
    path('addTask/', views.addTask, name='addTask'),
    path('markComplete/<int:pk>/', views.markComplete, name='markComplete'),
    path('markIncomplete/<int:pk>/', views.markIncomplete, name='markIncomplete'),
    path('deleteTask/<int:pk>/', views.deleteTask, name='deleteTask'),
    path('editTask/<int:pk>/', views.editTask, name='editTask'),
]