from django.http import HttpResponse
from django.shortcuts import render
from Djangotrain_app.models import Trains
import random

def index(request) :
    listtouslestrains = Trains.objects.all()  
    # listtouslestrains contient tous les trains de notre base de donnée 
    return render(request, "Djangotrain_app/index.html", {
        "listTrains" : listtouslestrains, 
        # pour afficher dans l'index html dans la boucle on va utiliser "listTrains" qui va donc contenir tous les trains de la base de donée
    })


def show(request, trains_id) : 
    listTrains = Trains.objects.get(trainId = trains_id) 
    # On va récupérer 1 train grace à son id parmi tous les trains de notre base de donnée 

    return render(request, "Djangotrain_app/show.html", {
        "Nom" : listTrains.name,  
        # meme fonctionnement que pour l'index on va utiliser Nom pour afficher le nom du train et nom name 
        "Ville" : listTrains.destination,
        "Découverte" : listTrains.overview,
        "preID" : int(trains_id) -1,
        #le bouton pour afficher le train précédent grace à l'ID
        "nextID" : int(trains_id) + 1,
        "time" : listTrains.time,
        "imagi" : listTrains.imagi,
        "ligne" : listTrains.ligne,
})



def hasard(request) :
    touslestrains = Trains.objects.all() 
    # pareil que index 
    trainhasard = random.choice(list(touslestrains))
    # fonction random qui choisi 1 seul train au hasard 
    return render(request, "Djangotrain_app/hasard.html", {
        "trainhasard" : trainhasard,
        # pareil que index et show, on utilise trainhasard pour afficher le train random sur la page hasard
    })

def recherche(request):
    lestrains = Trains.objects.all()

    text = request.GET.get('text')
    # on utilise.get pour récupérer la valeur écrit par l'utilisateur dans la barre de recherche, le nom de la barre de recherche est text.
   
    lestrains = Trains.objects.filter(destination__icontains=text) 
        # ici on filtre selon les différentes villes 
    return render(request, "Djangotrain_app/recherche.html",{
        'lestrains' : lestrains,
        'text' : text
    })