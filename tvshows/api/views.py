from rest_framework import viewsets
from .serializers import SeriesSerializer, ImageSerializer
from tvshows.models import Series, Image


class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()
    serializer_class = SeriesSerializer


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
