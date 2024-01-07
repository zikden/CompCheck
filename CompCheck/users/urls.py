from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name="profile"),
    path('authorization/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('authorization/', views.login, name="authorization"),
    path('password_reset/', views.password_reset, name="password_reset"),
]