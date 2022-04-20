from django import forms

from .models import Sortie

class SortieForm(forms.ModelForm):

    class Meta:
        model = Sortie
        fields = ('itineraire', 'duree_reelle','duree_reelle','nb_personne','niveaux','meteo','difficulte_reelle','date_de_sortie')