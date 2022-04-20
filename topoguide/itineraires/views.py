from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Itineraire, Sortie
from django.contrib.auth.decorators import login_required
# Create your views here.


def itineraires(request):
    #itineraires = Itineraire.objects.order_by()
    itineraires = get_list_or_404(Itineraire)
    return render(request, 'itineraires/itineraires.html', {'itineraires': itineraires})

def itineraire_details(request, itineraire_id):
    it = get_object_or_404(Itineraire, pk=itineraire_id)
    return render(request, 'itineraires/itineraire_details.html',{'it':it})