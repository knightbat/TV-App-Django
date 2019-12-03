from rest_framework import viewsets
from rest_framework.response import Response

from tvshows.api.serializers import EpisodeSerializer, SeriesSerializer, ImageSerializer
from tvshows.models import Series, Image, Episode
from rest_framework.decorators import action


class SeriesViewSet(viewsets.ModelViewSet):
    queryset = Series.objects.all()

    def get_serializer_class(self):
        if self.action == 'episodes':
            return EpisodeSerializer
        else:
            return SeriesSerializer

    @action(detail=True)
    def episodes(self, request, pk=None):
        series = Series.objects.get(pk=pk)
        eps = series.episodes.all()
        serializer = self.get_serializer(eps, many=True)
        return Response(serializer.data)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class EpisodeViewSet(viewsets.ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = EpisodeSerializer
