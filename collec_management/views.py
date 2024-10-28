from .models import Collec
from django.shortcuts import render,redirect, get_object_or_404
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

def add_collection(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        if title and description:
            Collec.objects.create(title=title, description=description)
            return render(request, 'add_collection.html', {'success_message': 'Collection ajoutée avec succès !'})
    
    return render(request, 'add_collection.html')


def delete_collection(request, collection_id):
    collection = get_object_or_404(Collec, id=collection_id)
    
    if request.method == "POST":
        collection.delete() 
        return redirect('all') 

    return render(request, 'delete_collection.html', {'collection': collection})

def update_collection(request,id):
    collec = get_object_or_404(Collec, pk=id)
    if request.method == 'POST':
        collec.title = request.POST.get('title')
        collec.description = request.POST.get('description')
        collec.save()
        return redirect('all')
    else:
        return render(request, 'update_collection.html',context={'collec':collec})
