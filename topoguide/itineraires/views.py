from django.shortcuts import get_list_or_404, get_object_or_404, render
from .models import Itineraire, Sortie
# Create your views here.
def itineraires_list(request):
    itineraires = Itineraire.objects.order_by()
    #itineraires = get_list_or_404(Itineraire)
    return render(request, 'itineraires/itineraires.html', {'itineraires': itineraires})