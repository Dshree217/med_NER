from django.contrib import admin
from django.urls import path
from search import views

urlpatterns = [
    path('search/', views.searchAPI),
    path("insert/", views.save_data)
]