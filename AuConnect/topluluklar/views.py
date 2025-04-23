from django.shortcuts import render
from django.http import HttpResponse

def liste(request):
    return render(request, "topluluklar/liste.html")