from rest_framework import serializers
from .models import Movie,Actor

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    opening_date = serializers.DateField()
    running_time = serializers.IntegerField()
    overview = serializers.CharField()

class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    gender = serializers.CharField()
    birth_date = serializers.DateField()