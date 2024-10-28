from django.shortcuts import render
from collec_management.models import *
from django.http import HttpResponse, Http404

# Create your views here.
def about(request):
    return render(request, "about.html")

def collection(request,collection_id):
    try:
        collection = Collec.objects.get(id=collection_id)
    except Collec.DoesNotExist:
        raise Http404("La collection n'existe pas.")
    return render(request,"collection.html",{"collection" : collection})

def all(request):
    collections = Collec.objects.order_by("date")
    context = {"all_collections" : collections}
    return render(request,"all.html",context)