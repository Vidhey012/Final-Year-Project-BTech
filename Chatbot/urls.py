from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('api', include("Chatbot.Api.urls")),
]
