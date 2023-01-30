from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets

from .models import Todo
from .serializers import TodosimpleSerializer,TodoDetailSerializer,TodoCreateSerializer

# Create your views here.

class TodosAPIView(APIView):
    def get(self,request):#전체조회
        todos = Todo.objects.filter(complete=False)
        serializer = TodosimpleSerializer(todos, many=True)
        return Response(serializer.data ,status=status.HTTP_200_OK)

    def post(self,request):#생성
        serializer = TodoCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TodoAPIView(APIView):#상세조최
    def get(slef,request,pk):
        todo = get_object_or_404(Todo,id=pk)
        serializer = TodoDetailSerializer(todo)
        return Response(serializer.data, status=status.HTTP_200_OK)