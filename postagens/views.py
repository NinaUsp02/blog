from django.http import HttpResponse
from .temp_data import postagem_data
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Postagem
from django.views import generic
from .forms import PostagemForm


def list_postagens(request):
    context = {"postagem_list": postagem_data}
    return render(request, "postagens/index.html", context)


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
        form = PostagemForm(request.POST)
        if form.is_valid():
            postagem_name = form.cleaned_data['name']
            postagem_release_year = form.cleaned_data['release_year']
            postagem_poster_url = form.cleaned_data['poster_url']
            postagem = Postagem(name=postagem_name,
                          release_year=postagem_release_year,
                          poster_url=postagem_poster_url)
            postagem.save()
            return HttpResponseRedirect(
                reverse('postagens:detail', args=(postagem.id, )))
    else:
        form = PostagemForm()
    context = {'form': form}
    return render(request, 'postagens/create.html', context)


def update_postagem(request, postagem_id):
    postagem = get_object_or_404(Postagem, pk=postagem_id)

    if request.method == "POST":
        form = PostagemForm(request.POST)
        if form.is_valid():
            postagem.name = form.cleaned_data['name']
            postagem.release_year = form.cleaned_data['release_year']
            postagem.poster_url = form.cleaned_data['poster_url']
            postagem.save()
            return HttpResponseRedirect(
                reverse('postagens:detail', args=(postagem.id, )))
    else:
        form = PostagemForm(
            initial={
                'name': postagem.name,
                'release_year': postagem.release_year,
                'poster_url': postagem.poster_url
            })

    context = {'postagem': postagem, 'form': form}
    return render(request, 'postagens/update.html', context)


def delete_postagem(request, postagem_id):
    postagem = get_object_or_404(Postagem, pk=postagem_id)

    if request.method == "POST":
        postagem.delete()
        return HttpResponseRedirect(reverse('Postagem:index'))

    context = {'postagem': postagem}
    return render(request, 'postagens/delete.html', context)