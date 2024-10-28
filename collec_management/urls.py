from django.urls import path
from . import views

urlpatterns = [
    path("about", views.about, name="about"),
    path("collection/<int:collection_id>",views.collection,name="collection"),
    path("all",views.all,name="all"),
     path('new', views.add_collection, name='add_collection'),
]