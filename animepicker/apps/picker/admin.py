from django.contrib import admin

from .models import Anime

class AnimeAdmin(admin.ModelAdmin):
    list_display = ('anime_title', 'anime_type', 'anime_genre', 'current_episodes', 'release_season', 'studio_name')
    list_filter = ['anime_type']
    search_fields = ['anime_title']

admin.site.register(Anime, AnimeAdmin)
