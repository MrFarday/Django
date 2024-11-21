from django.http import HttpResponse

def index(request):
    nama = "<h1> jauhari </h1>"
    kelas = "<h2> TIF </h2>"

    output = nama + kelas

    return HttpResponse(output)

def about(request):
    return HttpResponse('hallo2')