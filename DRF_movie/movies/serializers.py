from rest_framework import serializers
from .models import Movie,Actor

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True) #조회만하고싶다
#     name = serializers.CharField()
#     opening_date = serializers.DateField()
#     running_time = serializers.IntegerField()
#     overview = serializers.CharField()

#     def create(self,validated_data):
#         return Movie.objects.create(**validated_data) # 유효성 검사를 마친 데이터

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.opening_date = validated_data.get('opening_date',instance.opening_date)
#         instance.running_time = validated_data.get('running_time',instance.running_time)
#         instance.overview = validated_data.get('overview', instance.overview)
#         instance.save()
#         return instance

class MovieSerializer(serializers.ModelSerializer):#생성, 수정, 삭제 자동으로 만들어줌
    class Meta:
        model = Movie
        fields = ['id', 'name', 'opening_date', 'running_time', 'overview']


# class ActorSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     gender = serializers.CharField()
#     birth_date = serializers.DateField()

#     def create(self, validated_data):
#         return Actor.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name',instance.name)
#         instance.gender = validated_data.get('gender',instance.gender)
#         instance.birth_date = validated_data.get('birth_date',instance.birth_date)
#         instance.save()
#         return instance

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id','name','gender','birth_date']    