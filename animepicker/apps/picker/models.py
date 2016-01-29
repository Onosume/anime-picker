from django.db import models

class Anime(models.Model):
    """
    An anime property which can be a series, movie, OVA, net animation
    or something similar.
    """

    # Have choices for the anime type to allow searching
    TV = 'TV'
    MOVIE = 'Movie'
    OVA = 'OVA'
    ONA = 'ONA'
    SPECIAL = 'Special'

    ANIME_TYPE_CHOICES = (
        (TV, 'TV'),
        (MOVIE, 'Movie'),
        (OVA, 'OVA'),
        (ONA, 'ONA'),
        (SPECIAL, 'Special'),
    )

    # Build the model's fields
    anime_title = models.TextField(blank=True) # The official title of the anime
    alt_title = models.TextField(blank=True, null=True) # An alternate title, for example a shortened or translated title like 'Oreimo' or 'Attack on Titan'
    anime_type = models.CharField(max_length=10, choices=ANIME_TYPE_CHOICES, default=TV) # The anime type. TV, Movie, OVA, ONA, Special
    anime_genre = models.TextField(blank=True) # The anime's main genre, i.e. 'Slice of Life' or 'Action'
    current_episodes = models.IntegerField(default=0) # How many episodes does this anime currently have?
    max_episodes = models.IntegerField(default=0) # When complete how many episodes does this anime have? It is acceptable for long-running series that do not have a set number of episodes to have this set to zero
    release_season = models.CharField(max_length=15) # In what anime 'season' was this aniem first released? e.g. 'Summer 2013'
    studio_name = models.TextField(blank=True) # Who are the principal producers for this anime? e.g. 'Kyoto Animation' or 'Production I.G.'

    def __str__(self):
        return self.anime_title
