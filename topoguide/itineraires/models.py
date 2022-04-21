from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 


CHOICE1 = '0'
CHOICE2 = '1'
CHOICE3 = '2'

# Create your models here.
class Itineraire(models.Model):
   titre = models.CharField(max_length=200)
   depart = models.CharField(max_length=200)
   description = models.TextField() #texte de description du parcours
   altitude_depart = models.PositiveIntegerField("Altitude (en m)")
   altitude_min = models.PositiveIntegerField("Altitude minimum (en m)")
   altitude_max = models.PositiveIntegerField("Altitude maximum (en m)")
   denivele_pos = models.PositiveIntegerField("Dénivelé positif cumulé (en m")
   denivele_neg = models.PositiveIntegerField("Dénivelé négatif cumulé (en m")
   duree_estimee = models.FloatField("Durée estimée (en h)", validators=[MinValueValidator(0)])
   difficulte_estimee = models.PositiveIntegerField("Difficulté estimée (de 1 à 5)",default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    
   def __str__(self):
      return self.titre
     
     
class Sortie(models.Model):
   utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
   itineraire = models.ForeignKey('Itineraire', on_delete=models.CASCADE)
   duree_reelle = models.FloatField("Durée réelle (en h)",validators=[MinValueValidator(0)])
   nb_personne = models.PositiveIntegerField("Nombre de personnes ayant participé à la sortie")
   
   ## attribut expérience du groupe
   NIVEAUX = [(CHOICE1, ('Tous débutants')),
      (CHOICE2, ('Mixte')),
      (CHOICE3, ('Tous experts')),]
   niveaux = models.CharField("Niveau des personnes", max_length=32, choices=NIVEAUX)
   
   ##attribut météo 
   METEO = [(CHOICE1, ('Bonne météo')),
      (CHOICE2, ('Météo moyenne')),
      (CHOICE3, ('Mauvaise météo')),]
   meteo = models.CharField("Météo", max_length=32, choices=METEO)
   
   difficulte_reelle  = models.IntegerField("Difficulté ressentie (de 1 à 5)",default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
   date_de_sortie = models.DateField("Date de sortie")
   
   def __str__(self):
        return str(self.itineraire)+" - par " + str(self.utilisateur)

