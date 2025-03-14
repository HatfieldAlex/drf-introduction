from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Character
from .serializers import CharacterSerializer

@api_view(['GET'])
def character_list(request):
    characters = Character.objects.all()
    serializer = CharacterSerializer(characters, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
