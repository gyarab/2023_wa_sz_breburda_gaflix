from django.contrib import admin
from filmy.models import Movie, Director, Genre, Actor

class MovieLoader(admin.ModelAdmin):
    list_display = ['id', 'name', 'year', 'footage', 'genres_display', 'director']
    list_display_links = ['id', 'name']
    search_fields = ['name', 'director_name']
    list_filter = ['genres', 'year']

class MovieAdmin(admin.ModelAdmin):
    pass

class DirectorAdmin(admin.ModelAdmin):
    pass

class GenreAdmin(admin.ModelAdmin):
    pass

class ActorAdmin(admin.ModelAdmin):
    pass

admin.site.register(Movie, MovieAdmin)

admin.site.register(Director, DirectorAdmin)

admin.site.register(Genre, GenreAdmin)

admin.site.register(Actor, ActorAdmin)