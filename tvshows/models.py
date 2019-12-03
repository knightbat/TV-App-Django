from django.db import models

class Image(models.Model):
    medium = models.CharField(max_length=200)
    original = models.CharField(max_length=200)


class Series(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    language = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    runtime = models.IntegerField()
    premiered = models.DateField()
    officialSite = models.CharField(max_length=200)
    weight = models.IntegerField()
    summary = models.TextField()
    image = models.OneToOneField(
        Image,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return self.name


class Season(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200, blank=True)
    episodeOrder = models.IntegerField()
    premiereDate = models.DateField()
    endDate = models.DateField()
    # network = models.CharField(max_length=200)
    webChannel = models.CharField(max_length=200, blank=True, null=True)
    summary = models.CharField(max_length=200, blank=True)
    image = models.OneToOneField(
        Image,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    series = models.ForeignKey(Series, on_delete=models.CASCADE, blank=True, null=True, related_name='seasons')

    def __str__(self):

        name = self.series.name if self.series.name else ""
        return f'{name} - {self.number}'


class Episode(models.Model):
    episodeName = models.CharField(max_length=200, blank=True)
    airedSeason = models.IntegerField()
    episodeNumber = models.IntegerField()
    airdate = models.DateField()
    airtime = models.TimeField()
    runtime = models.CharField(max_length=200)
    summary = models.CharField(max_length=200)
    image = models.OneToOneField(
        Image,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    series = models.ForeignKey(Series, on_delete=models.CASCADE, blank=True, null=True, related_name='episodes')

    def __str__(self):
        name = self.series.name if self.series.name else ""
        return f'{name} - S{self.airedSeason}E{self.episodeNumber}'
