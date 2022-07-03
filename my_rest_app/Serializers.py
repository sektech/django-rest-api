from rest_framework import serializers
from my_rest_app.models import *

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('name', 'birth_year', 'eye_color', 'species')

class SpeicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Species
        fields = ('name', 'classification', 'language')
