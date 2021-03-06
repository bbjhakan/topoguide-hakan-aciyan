from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from .models import Itineraire, Sortie
from .forms import SortieForm
from django.contrib.auth.decorators import login_required
# Create your views here.

#Vue avec une liste des itinéraires
def itineraires(request):
    itineraires = get_list_or_404(Itineraire)
    
    return render(request, 'itineraires/itineraires.html', {'itineraires': itineraires})


#Vue pour les détails sur un itinéraire
def itineraire_details(request, itineraire_id):
    it = get_object_or_404(Itineraire, pk=itineraire_id)
    
    #J'ajoute les variable h et mn (et les ajoute dans le contexte) pour pouvoir afficher l'heure d'une manière plus jolie car mon attribut duree_estimee est un float
    h = int(it.duree_estimee) 
    mn = int((it.duree_estimee-h)*60)
    
    sorties = Sortie.objects.filter(itineraire_id=itineraire_id)
    
    return render(request, 'itineraires/itineraire_details.html',{'it':it, 'sorties':sorties,'heure':h, 'minute':mn})


#Vue pour les détails sur une sortie
def sortie(request, sortie_id):
    sortie = get_object_or_404(Sortie, pk=sortie_id)
    attributs = Sortie.objects.filter(id=sortie_id)
    
    #J'ajoute les variable h et mn pour pouvoir afficher l'heure d'une manière plus jolie car mon attribut duree_estimee est un float (bien évidemment, l'itinéraire dure au moins 1 heure)
    h = int(sortie.duree_reelle) 
    mn = int((sortie.duree_reelle-h)*60)
    
    ##Les deux variables qui suivent sont pour comparer avec les données estimées
    h_it = int(sortie.itineraire.duree_estimee) 
    mn_it = int((sortie.itineraire.duree_estimee-h_it)*60)
    
    #Ajout dans le contexte de s (qui donne "nom de la sortie - par utilisateur") pour pouvoir faire une barre de navigation lisible (voir sortie.html)
    return render(request, 'itineraires/sortie.html', {'sortie':sortie, 'attributs':attributs, 's': str(sortie),'heure':h, 'minute':mn,'hit':h_it, 'mnit': mn_it}) 


#Vue pour créer une nouvelle sortie avec un formulaire
@login_required
def nouvelle_sortie(request, itineraire_id):
    itineraire = get_object_or_404(Itineraire, pk=itineraire_id)
    
    if request.method == "POST":
        form = SortieForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.utilisateur = request.user
            post.itineraire = itineraire
            post.save()
            
            return redirect('../')
    else:
        form = SortieForm()
        
    return render(request, 'itineraires/nouvelle_sortie.html', {'form': form, 'itineraire': itineraire})


#Vue pour modifier une sortie avec un formulaire pré-rempli  
@login_required
def modifier_sortie(request, sortie_id):
    sortie = get_object_or_404(Sortie, pk=sortie_id)
    if request.method == "POST":
        form = SortieForm(request.POST, instance=sortie)
        if form.is_valid():
            sortie = form.save(commit=False)
            sortie.utilisateur = request.user
            sortie.save()
            
            return redirect(f"../{sortie_id}", pk=sortie.pk)
    else:
        form = SortieForm(instance=sortie)
        
    #Ajout dans le contexte de s (qui donne "nom de la sortie - par utilisateur") pour pouvoir faire une barre de navigation lisible (voir sortie_edit.html)
    return render(request, 'itineraires/sortie_edit.html', {'form': form, 'sortie':sortie, 's': str(sortie)})