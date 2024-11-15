from django.db import models
from django.conf import settings
from django.utils import timezone


class Postagem(models.Model):
    name = models.CharField(max_length=255)
    release_year = models.IntegerField()
    poster_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return f'{self.name} ({self.release_year})'


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    postagem = models.ForeignKey(Postagem, on_delete=models.CASCADE)
    data_postagem = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['-data_postagem']
    def __str__(self):
        return f'"{self.text}" - {self.author.username}'
    

class Category(models.Model):
    name = models.CharField(max_length=225)
    description = models.TextField() 
    postagens = models.ManyToManyField(Postagem)

    def __str__(self):
        return f'{self.name}'
    
