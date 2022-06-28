from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def heading(request):
    my_dict = {'insert_me':"Now I am Coming from first_app/index.html"}
    return HttpResponse("Hello World!!!!")
