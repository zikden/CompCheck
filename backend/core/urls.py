from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.main.urls')),
    path('profile/', include('app.users.urls')),
    path('archive/', include('app.archive.urls')),
    path('components/', include('app.components.urls'))
]
