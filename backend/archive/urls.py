from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views
from .views import ProcessorViewSet, VideoCardViewSet

router = SimpleRouter()
router.register(r'archive_processor', ProcessorViewSet)
router.register(r'archive_videocard', VideoCardViewSet)

urlpatterns = [
    path('', views.archive, name="archive"),
    path('CPU/', views.CPU, name="CPU"),
    path('GPU/', views.GPU, name="GPU"),
]
urlpatterns += router.urls
