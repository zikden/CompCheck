from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('profile/', include('users.urls')),
    path('archive/', include('app.archive.urls')),
    path('components/', include('app.components.urls'))
]
