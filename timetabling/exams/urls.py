from django.urls import path
from exams import views

urlpatterns = [
    path('', views.index),
]
