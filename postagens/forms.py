from django.forms import ModelForm
from .models import Postagem


class PostagemForm(ModelForm):
    class Meta:
        model = Postagem
        fields = [
            'name',
            'release_year',
            'poster_url',
        ]
        labels = {
            'name': 'Título',
            'release_year': 'Data de Início',
            'poster_url': 'URL do Poster',
        }