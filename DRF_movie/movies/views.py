from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Movie
from .serializers import MovieSerializer

# Create your views here.
# @api_view(['GET'])으로 함수형 뷰인 movie_list()가 GET 메소드만 허용하는 API를 제공한다는 걸 표시
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objests.all()
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data, status=200)