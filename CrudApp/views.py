from django.shortcuts import render,redirect,HttpResponse
from .models import Candidat

# Create your views here.
def index(request):
    Candidats = Candidat.objects.all()
    context = {
        'Candidats': Candidats,
    }
    return render(request,'index.html',context)

def selection(request):
    Candidats = Candidat.objects.all()

    context = {
        'Candidats': Candidats,
    }
    return render(request,'selection.html',context)

def listes_S(request):
    Candidats = Candidat.objects.filter(Result="Sélectionner")

    context = {
        'Candidats': Candidats,
    }
    return render(request,'listes_S.html',context)

def listes_NS(request):
    Candidats = Candidat.objects.filter(Result="Non Sélectionner")

    context = {
        'Candidats': Candidats,
    }
    return render(request,'listes_NS.html',context)

def create(request):
    print(request.POST)
    nom = request.GET['Nom']
    prenom = request.GET['Prenom']
    note_HG = request.GET['Note_HG']
    note_ANG = request.GET['Note_ANG']
    note_FR = request.GET['Note_FR']
    create_candt = Candidat(Nom = nom,Prenom = prenom,Note_HG = note_HG,Note_ANG = note_ANG,Note_FR = note_FR)
    create_candt.save()
    return redirect('/index')

def edit(request,id):
    Candidats = Candidat.objects.get(pk=id)
    context = {
        'Candidats': Candidats
    }
    return render(request,'edit.html',context)

def delete(request,id):
    Candidats = Candidat.objects.get(pk=id)
    Candidats.delete()
    return redirect('/index')

def update(request,id):
    Cand = Candidat.objects.get(pk=id)
    Cand.Nom = request.GET['Nom']
    Cand.Prenom = request.GET['Prenom']
    Cand.Note_HG = request.GET['Note_HG']
    Cand.Note_ANG = request.GET['Note_ANG']
    Cand.Note_FR = request.GET['Note_FR']
    Cand.save()
    return redirect('/index')

