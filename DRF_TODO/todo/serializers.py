from rest_framework import serializers
from .models import Todo

class TodosimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title','complete','important')