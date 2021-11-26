from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponce("Здесь будет выведен список объявлений.")
