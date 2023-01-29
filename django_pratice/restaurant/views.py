from django.shortcuts import render
from django.http import HttpResponse
from datetime  import datetime
# Create your views here.

def index(request):
    today = datetime.today().date()
    context = {"date": today}
    return render(request,'restaurant/index.html',context=context)

def food_detail(request,food):
    context = {"name": food}
    return render (request,'restaurnat/detail.html',context=context)