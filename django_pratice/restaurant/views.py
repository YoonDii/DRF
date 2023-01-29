from django.shortcuts import render
from django.http import HttpResponse
from datetime  import datetime
# Create your views here.

def index(request):
    today = datetime.today()
    print(today)
    return render(request,'restaurant/index.html')