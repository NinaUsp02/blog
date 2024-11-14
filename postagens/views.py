from django.http import HttpResponse
from .temp_data import postagem_data
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Postagem


def list_postagens(request):
    postagem_list = Postagem.objects.all()
    context = {'postagem_list': postagem_list}
    return render(request, 'postagens/index.html', context)

def detail_postagem(request, postagem_id):
    postagem = get_object_or_404(Postagem, pk=postagem_id)
    context = {'postagem': postagem}
    return render(request, 'postagens/detail.html', context)

def search_postagens(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        postagem_list = Postagem.objects.filter(name__icontains=search_term)
        context = {"postagem_list": postagem_list}
    return render(request, 'postagens/search.html', context)

def create_postagem(request):
    if request.method == 'POST':
        postagem_name = request.POST['name']
        postagem_release_year = request.POST['release_year']
        postagem_poster_url = request.POST['poster_url']
        postagem = Postagem(name=postagem_name,
                      release_year=postagem_release_year,
                      poster_url=postagem_poster_url)
        postagem.save()
        return HttpResponseRedirect(
            reverse('postagens:detail', args=(postagem.id, )))
    else:
        return render(request, 'postagens/create.html', {})