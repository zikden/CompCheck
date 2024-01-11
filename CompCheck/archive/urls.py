from django.urls import path
from . import views

urlpatterns = [
    path('', views.archive, name="archive"),
    path('CPU/', views.CPU, name="CPU"),
    path('GPU/', views.GPU, name="GPU"),
]