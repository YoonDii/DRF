from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Movie , Actor
from .serializers import MovieSerializer,ActorSerializer

# Create your views here.
# @api_view(['GET'])으로 함수형 뷰인 movie_list()가 GET 메소드만 허용하는 API를 제공한다는 걸 표시
@api_view(['GET','POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data 
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def actor_list(request):
    actors = Actor.objects.all()
    serializer = ActorSerializer(actors, many =True)
    return Response(serializer.data, status=200)