from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('1', views.show, name='show'), # Sample route added just to familiarize myself - #ToBeRemoved
]