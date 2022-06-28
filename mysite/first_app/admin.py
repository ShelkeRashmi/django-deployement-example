from django.contrib import admin
from django.http import HttpResponse

# Register your models here.

def heading(request):
    return HttpResponse("Helloooooo!!!!!!Welcome!!!!1")
