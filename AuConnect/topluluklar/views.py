from django.shortcuts import render
from django.http import HttpResponse
from .models import Topluluklar

def liste(request):

    topluluklar = Topluluklar.objects.all()
    context = {
        "topluluklar" : topluluklar
    }


    return render(request, "topluluklar/liste.html", context)