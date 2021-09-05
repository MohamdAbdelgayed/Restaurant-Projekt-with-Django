from django.urls import path
from . import views

app_name = 'bestellung'

urlpatterns = [
    path('', views.index, name='index'),
    path('einkaufskorb/', views.einkaufskorb, name='einkaufskorb'),
]
