from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. You are at Chai aur Django homepage")
    return render(request, 'website/index.html')

def about(request):
    return HttpResponse("Hello, world. You are at Chai aur Django about page")

def info(request):
    return HttpResponse("Hello, world. You are at Chai aur Django contact page")