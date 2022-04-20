from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

# Create your models here.
class Itineraire(models.Model):
    titre = models.CharField(max_length=200)
    depart = models.CharField(max_length=200)
    description = models.TextField()
    altitude_depart = models.IntegerField("Altitude (en m)")
    altitude_min = models.IntegerField("Altitude minimum (en m)")
    altitude_max = models.IntegerField("Altitude maximum (en m)")
    denivele_pos = models.IntegerField("Dénivelé positif cumulé (en m")
    denivele_neg = models.IntegerField("Dénivelé négatif cumulé (en m")
    duree_estimee = models.FloatField("Durée estimée (en h)")
    difficulte_estimee = models.IntegerField("Difficulté estimée (de 1 à 5)",default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
    def __str__(self):
        return self.titre
     
     
class Sortie(models.Model):
   utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
   itineraire = models.ForeignKey('Itineraire', on_delete=models.CASCADE)
   duree_reelle = models.FloatField("Durée réelle (en h)")
   nb_personne = models.IntegerField("Nombre de personnes ayant participé à la sortie")
    
   ## attribut expérience du groupe

   NIVEAUX = [('0', ('Tous débutants')),
      ('1', ('Mixte')),
      ('2', ('Tous experts')),]
   niveaux = models.CharField("Niveau des personnes", max_length=32, choices=NIVEAUX)

    
   METEO = [('0', ('Bonne météo')),
      ('1', ('Météo moyenne')),
      ('2', ('Mauvaise météo')),]
   meteo = models.CharField("Météo", max_length=32, choices=METEO)
   difficulte_reelle  = models.IntegerField("Difficulté ressentie (de 1 à 5)",default=0, validators=[MinValueValidator(0), MaxValueValidator(5)])
   date_de_sortie = models.DateField("Date de sortie")

