from django.urls import path, include
from . import views
from .api import urls

app_name = 'tvshows'
urlpatterns = [
    path('', views.index, name='tvshows-index'),
    path('<int:id>/', views.details, name='tvshows-details'),

    path('api/', include(urls), name='tvshows-list-api'),

]
