from django.shortcuts import render
from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
from app01 import models


def test(request):

    return HttpResponse("OK，你看什么事情都没有发生")


def home(request):
    return render(request,'home.html')



