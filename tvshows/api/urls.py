from django.urls import path, include
from .views import SeriesViewSet, ImageViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('series', SeriesViewSet)
router.register('images', ImageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]