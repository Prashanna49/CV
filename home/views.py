from django.http import HttpResponse
from django.shortcuts import render
#from django.http import HttpResponse

def home(request):
    return render(request, "index.html")

def about(request):
    return HttpResponse ("Welcome to About Page")

def contact(request):
    return HttpResponse ("Welcome to Contact Page")
    