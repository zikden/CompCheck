from django.urls import path
from . import views

urlpatterns = [
    path('', views.ComponentsViews, name="ComponentsViews"),
]
