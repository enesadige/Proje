from django.shortcuts import render
from django.http import HttpResponse
from .models import Topluluklar
from django.http import Http404  

def liste(request):

    topluluklar = Topluluklar.objects.all()
    context = {
        "topluluklar" : topluluklar
    }
    return render(request, "topluluklar/liste.html", context)


def detail(request, topluluklar_id):
    try:
        topluluklar = Topluluklar.objects.get(pk = topluluklar_id)
    except Topluluklar.DoesNotExist:
        raise Http404('Topluluk bulunamadı...')
    
    context = {
        'topluluklar':topluluklar
    }
    return render(request, "topluluklar/detail.html", context)