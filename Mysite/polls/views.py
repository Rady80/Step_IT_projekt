from django.http import HttpResponse
from django.shortcuts import render

# Zde si vytvořte své pohledy.

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")