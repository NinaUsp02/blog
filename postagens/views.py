from django.http import HttpResponse
from .temp_data import postagem_data
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def detail_postagem(request, postagem_id):
    postagem = postagem_data[postagem_id - 1]
    return HttpResponse(
        f'Detalhes do projeto {postagem["name"]} ({postagem["release_year"]})')

def list_postagens(request):
    context = {"postagem_list": postagem_data}
    return render(request, 'postagens/index.html', context)

def detail_postagem(request, postagem_id):
    context = {'postagem': postagem_data[postagem_id - 1]}
    return render(request, 'postagens/detail.html', context)

def search_postagens(request):
    context = {}
    if request.GET.get('query', False):
        context = {
            "postagem_list": [
                m for m in postagem_data
                if request.GET['query'].lower() in m['name'].lower()
            ]
        }
    return render(request, 'postagens/search.html', context) 


def create_postagem(request):
    if request.method == 'POST':
        postagem_data.append({
            'name': request.POST['name'],
            'release_year': request.POST['release_year'],
            'poster_url': request.POST['poster_url']
        })
        return HttpResponseRedirect(
            reverse('postagens:detail', args=(len(postagem_data), )))
    else:
        return render(request, 'postagens/create.html', {})