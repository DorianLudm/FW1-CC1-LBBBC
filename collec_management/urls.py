from django.urls import path
from . import views

urlpatterns = [
    path("", views.accueil, name="accueil"),
    path("about", views.about, name="about"),
    path("collection/<int:collection_id>",views.collection,name="collection"),
    path("all",views.all,name="all"),
    path('new', views.add_collection, name='add_collection'),
    path('delete/<int:collection_id>/', views.delete_collection, name='delete_collection'),
    path('change/<id>', views.update_collection, name='update_collection'),
]