from rest_framework import serializers
from tvshows.models import Series, Image


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class SeriesSerializer(serializers.ModelSerializer):

    image = ImageSerializer(many=False)

    class Meta:
        model = Series
        fields = '__all__'

    def create(self, validated_data):
        image_data = validated_data.pop('image')
        image = Image.objects.create(**image_data)
        series = Series.objects.create(**validated_data, image=image)
        return series

    def update(self, instance, validated_data):

        image_data = validated_data.pop('image')
        image = instance.image

        instance.name = validated_data.get('name', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.language = validated_data.get('language', instance.language)
        instance.status = validated_data.get('status', instance.status)
        instance.runtime = validated_data.get('runtime', instance.runtime)
        instance.premiered = validated_data.get('premiered', instance.premiered)
        instance.officialSite = validated_data.get('officialSite', instance.officialSite)
        instance.weight = validated_data.get('weight', instance.weight)
        instance.summary = validated_data.get('summary', instance.summary)
        instance.save()

        image.medium = image_data.get('medium', image.medium)
        image.original = image_data.get('original', image.original)
        image.save()
        return instance
