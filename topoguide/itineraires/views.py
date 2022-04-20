from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from .models import Itineraire, Sortie
from .forms import SortieForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def itineraires(request):
    #itineraires = Itineraire.objects.order_by()
    itineraires = get_list_or_404(Itineraire)
    return render(request, 'itineraires/itineraires.html', {'itineraires': itineraires})

def itineraire_details(request, itineraire_id):
    it = get_object_or_404(Itineraire, pk=itineraire_id)
    sorties = Sortie.objects.filter(itineraire_id=itineraire_id)
    return render(request, 'itineraires/itineraire_details.html',{'it':it, 'sorties':sorties})

def nouvelle_sortie(request):
    if request.method == "POST":
        form = SortieForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.utilisateur = request.user
            post.save()
            return redirect('../itineraires')
    else:
        form = SortieForm()
    return render(request, 'itineraires/nouvelle_sortie.html', {'form': form})
        