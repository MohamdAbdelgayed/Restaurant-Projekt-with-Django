from django.urls import path
from . import views

app_name = 'tos'
urlpatterns = [
    path('', views.index, name='index')
]
