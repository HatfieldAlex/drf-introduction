from django.contrib import admin
from .models import Character

@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')            # Show these fields in the list view
    search_fields = ('name',)                # Add a search box on the name field
    ordering = ('name',)                     # Order alphabetically by default
