from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from my_rest_app.models import Person
from my_rest_app.Serializers import *


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class SpeciesViewSet(viewsets.ModelViewSet):
    queryset = Species.objects.all()
    serializer_class = SpeicesSerializer
