from rest_framework import serializers
from .models import Character

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ['id', 'name']

"""
The serializer is critical to DRF. Unlike regular Django where data is exposed to HTML through templates, DRF needs to convert data into JSON format. Serializers handle this transformation.
"""