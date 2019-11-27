from django.contrib import admin
from .models import Series, Image, Season, Episode


admin.site.register(Series)
admin.site.register(Image)
admin.site.register(Season)
admin.site.register(Episode)
