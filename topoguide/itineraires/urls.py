from django.urls import path

from . import views

app_name = 'itineraires'

urlpatterns = [
    path('',views.itineraires_list, name='itineraires_list')
]