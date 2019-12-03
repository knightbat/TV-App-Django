from django.shortcuts import render, get_object_or_404
from .models import Series


def index(request):
    series_list = Series.objects.all()
    context = {
        'series_list': series_list,
        'title': 'Home',
    }
    return render(request, 'tvshows/index.html', context)


def details(request, id):
    series = get_object_or_404(Series, pk=id)
    context = {
        'series': series,
        'title': series.name,
        # 'seasons': series.seasons.all(),
    }
    return render(request, 'tvshows/details.html', context)



