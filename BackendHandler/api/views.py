from django.shortcuts import render
from django.http import HttpResponse

def APi(request):
    return HttpResponse("Hello, World! from API")
# Create your views here.
