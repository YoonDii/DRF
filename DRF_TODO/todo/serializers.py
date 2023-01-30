from rest_framework import serializers
from .models import Todo

#전체조회
class TodosimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title','complete','important')

#상세조회
class TodoDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=Todo
        fields = ('id','title','description','created','complete','important')

#생성
class TodoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title','description','important')