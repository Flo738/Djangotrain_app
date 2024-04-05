from django.http import HttpResponse
from django.shortcuts import render
from Djangotrain_app.models import Trains

def index(request) :
    listtouslestrains = Trains.objects.all()

    return render(request, "Djangotrain_app/index.html", {
        "listTrains" : listtouslestrains,
    })


def show(request, trains_id) : 
    listTrains = Trains.objects.get(trainId = trains_id)
    Trains_screen = listTrains 

    return render(request, "Djangotrain_app/show.html", {
        "Nom" : Trains_screen.name,
        "Ville" : Trains_screen.destination,
        "Découverte" : Trains_screen.overview,
        "nextID" : int(trains_id) + 1,
})