# Projet Django - Gestionnaire de collections

## Membres
Prénom | NOM | Adresse universitaire  
Dorian LUDMANN dorian.ludmann@etu.univ-orleans.fr    
Theo Benet-Chapard theo.benet-chapard@etu.univ-orleans.fr  
Ayoub BOUAYA ayoub.bouaya@etu.univ-orleans.fr  
Ayoub BAHI ayoub.bahi@etu.univ-orleans.fr  

## Commandes d'initialisation
```bash
# Initialisation du projet et de l'application
django-admin startproject cc
cd cc
python manage.py startapp collec_management
```

On rajoute la nouvelle application des les settings du projet
```py
# cc/settings.py
INSTALLED_APPS = [
    ...
    'collec_management',
]
```

```bash
# Lancement du projet
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
```

## Création d'un objet de classe Collec
```bash
python manage.py shell
```

```py
from collec_management.models import Collec
from django.utils import timezone
Collec.objects.all()
#<QuerySet []> -> table vide
c=Collec(title="Liste.",description="Ceci est ma collection Liste.",date=timezone.now())
c.id
c.save()
Collec.objects.all()
#<QuerySet [<Collec: Liste>]> -> table avec un objet de classe Collec
quit()
```

## Installation de Django-Bootstrap5
```bash
python3 -m pip install django-bootstrap5
```
