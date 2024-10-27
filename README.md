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
