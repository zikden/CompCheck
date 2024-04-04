from django.urls import path
from . import views

urlpatterns = [
    path('', views.components, name="components"),
]
