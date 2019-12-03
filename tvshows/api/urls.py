from django.urls import path, include

from tvshows.api.views import EpisodeViewSet, SeriesViewSet, ImageViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('series', SeriesViewSet)
router.register('images', ImageViewSet)
router.register('episodes', EpisodeViewSet)


urlpatterns = [
    path('', include(router.urls)),
]