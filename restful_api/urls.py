from django.urls import path
from .views import character_list, CharacterCreate

urlpatterns = [
    path('characters/list/', character_list, name='character-list'),
    path('characters/create/', CharacterCreate.as_view(), name='character-create'),
]
