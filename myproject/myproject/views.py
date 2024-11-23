from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'judul':'kelas MJ',
        'kontributor':'MJ',
    }
    return render(request,'index.html', context)

