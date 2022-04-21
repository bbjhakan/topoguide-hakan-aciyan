from django import forms

from .models import Sortie

class SortieForm(forms.ModelForm):
    #Formulaire pour créer/éditer une sortie liée à un itinéraire
    class Meta:
        model = Sortie
        fields = ('duree_reelle','duree_reelle','nb_personne','niveaux','meteo','difficulte_reelle','date_de_sortie')