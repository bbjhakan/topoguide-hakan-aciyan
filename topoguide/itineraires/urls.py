from django.urls import path

from . import views


urlpatterns = [
    path('',views.itineraires, name='itineraires'),
    path('<int:itineraire_id>/', views.itineraire_details, name='itineraire_details'),
    path('sortie/<int:sortie_id>',views.sortie, name='sortie'),
    path('nouvelle_sortie/', views.nouvelle_sortie, name='nouvelle_sortie'),
    path('sortie/<int:sortie_id>/edit',views.modifier_sortie, name='modifier_sortie')
]