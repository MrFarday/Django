from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {
        'judul':'blog mj',
        'kontributor':'mj 2',
    }
    return  render(request, "blog/index.html", context)

def cerita(request):
    context = {
        'judul':'cerita',
        'kontributor':'otong',
    }
    return  render(request, "blog/index.html", context)

def news(request):
    context = {
        'judul':'news',
        'kontributor':'jajang',
    }
    return  render(request, "blog/index.html", context)
