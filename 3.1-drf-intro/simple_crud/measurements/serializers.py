# TODO: опишите сериализаторы
from rest_framework import serializers
from .models import Project, Measurement


class ProjectModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class MeasurementModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = '__all__'
