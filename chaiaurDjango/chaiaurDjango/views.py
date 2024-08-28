from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello, world. You are at Chai aur Django homepage")
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def info(request):
    return render(request, 'website/info.html')