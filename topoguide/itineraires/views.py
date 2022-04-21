from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from .models import Itineraire, Sortie
from .forms import SortieForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def itineraires(request):
    itineraires = get_list_or_404(Itineraire)
    
    return render(request, 'itineraires/itineraires.html', {'itineraires': itineraires})

#Vue pour les détails sur un itinéraire
def itineraire_details(request, itineraire_id):
    it = get_object_or_404(Itineraire, pk=itineraire_id)
    sorties = Sortie.objects.filter(itineraire_id=itineraire_id)
    
    return render(request, 'itineraires/itineraire_details.html',{'it':it, 'sorties':sorties})

#Vue pour les détails sur une sortie
def sortie(request, sortie_id):
    sortie = get_object_or_404(Sortie, pk=sortie_id)
    attributs = Sortie.objects.filter(id=sortie_id)
    
    #Ajout dans le context de s pour pouvoir faire une barre de navigation lisible (voir sortie.html)
    return render(request, 'itineraires/sortie.html', {'sortie':sortie, 'attributs':attributs, 's': str(sortie)}) 

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
        
    #Ajout dans le context de s pour pouvoir faire une barre de navigation lisible (voir sortie_edit.html)
    return render(request, 'itineraires/sortie_edit.html', {'form': form, 'sortie':sortie, 's': str(sortie)})