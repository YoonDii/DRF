from rest_framework import serializers
from .models import Movie,Actor

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True) #조회만하고싶다
    name = serializers.CharField()
    opening_date = serializers.DateField()
    running_time = serializers.IntegerField()
    overview = serializers.CharField()

    def create(self,validated_data):
        return Movie.objects.create(**validated_data) # 유효성 검사를 마친 데이터


class ActorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    gender = serializers.CharField()
    birth_date = serializers.DateField()

    def create(self, validated_data):
        return Actor.objects.create(**validated_data)