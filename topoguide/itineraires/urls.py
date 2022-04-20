from django.urls import path

from . import views

app_name = 'itineraires'

urlpatterns = [
    path('',views.itineraires, name='itineraires'),
    path('<int:itineraire_id>/', views.itineraire_details, name='itineraire_details')
]