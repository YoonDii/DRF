from django.urls import path, include
from project.views import HelloAPI, bookAPI,booksAPI,BookAPI, BooksAPI #소문자book은 함수형, 대문자book은 클래스형

urlpatterns = [
    path("hello/", HelloAPI),
    path('fbv/books/',booksAPI),
    path('fbv/book/<int:bid>/',bookAPI),
    path('cbv/books/',BooksAPI.as_view()),
    path('cbv/book/<int:bid>/',BookAPI.as_view()),
]
