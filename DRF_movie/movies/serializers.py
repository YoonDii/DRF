from rest_framework import serializers
from rest_framework.serializers import ValidationError
from django.core.validators import MaxLengthValidator,MinLengthValidator #길이제한 유효성검사.
from rest_framework.validators import UniqueTogetherValidator #두 개 이상의 필드에서 값이 유일한지 확인.
from .models import Movie,Actor,Review

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

#유효성검사 직접 작성하기
def overview_validator(value):
    if value > 300:
        raise ValidationError('소개 문구는 최대 300자 이하로 작성해야 합니다.')
    elif value < 10:
        raise ValidationError('소개 문구는 최소 10자 이상으로 작성해야 합니다.')
    return value

class MovieSerializer(serializers.ModelSerializer):#생성, 수정, 삭제 자동으로 만들어줌
    class Meta:
        model = Movie
        fields = ['id', 'name', 'opening_date', 'running_time', 'overview']
        #유효성검사도구 사용시
        # overview = serializers.CharField(validators=[MinLengthValidator(limit_value=10), MaxLengthValidator(limit_value=300)])
        #유효성검사 직접작성
        overview = serializers.CharField(validators=[overview_validator])
        validators = [UniqueTogetherValidator(queryset=Movie.objects.all(),fields=['name','overview'])]
        # fields는 queryset에서 조회한 데이터 중 어떤 필드들을 기준으로 유일성 검사를 할지 정의하는 필수 옵션

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


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','movie','username','star','comment','created']
        # extra_kwargs 옵션으로 리뷰를 생성할 때는 영화 정보(id)를 입력받지 않고 URL로 받아올 것
        extra_kwargs = {
            'movie':{'read_only': True},
        }