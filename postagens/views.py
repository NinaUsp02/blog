from django.http import HttpResponse
from .temp_data import postagem_data
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Postagem
from django.views import generic


class PostagemListView(generic.ListView):
    model = Postagem
    template_name = 'postagens/index.html'

class PostagemDetailView(generic.DetailView):
    model = Postagem
    template_name = 'postagens/detail.html'
    context_object_name = 'postagem'

class PostagemSearchView(generic.ListView):
    model = Postagem
    template_name = 'postagens/search.html'
    context_object_name = 'postagem_list'

    def get_queryset(self):
        query = self.request.GET.get('query', '').lower()
        if query:
            return Postagem.objects.filter(name__icontains=query)
        return Postagem.objects.none()

class PostagemCreateView(generic.CreateView):
    model = Postagem
    template_name = 'postagens/create.html'
    fields = ['name', 'release_year', 'poster_url']
    def form_valid(self, form):
        response = super().form_valid(form)
        success_url = reverse('postagens:detail', kwargs={'pk': self.object.pk})
        return HttpResponseRedirect(success_url)
    
class PostagemUpdateView(generic.UpdateView):
    model = Postagem
    template_name = 'postagens/update.html'
    fields = ['name', 'release_year', 'poster_url']
    def form_valid(self, form):
        response = super().form_valid(form)
        success_url = reverse('postagens:detail', kwargs={'pk': self.object.pk})
        return HttpResponseRedirect(success_url)

class PostagemDeleteView(generic.DeleteView):
    model = Postagem
    template_name = 'postagens/delete.html'
    def get_success_url(self):
        return reverse('postagens:index')

""" def detail_postagem(request, postagem_id):
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


def update_postagem(request, postagem_id):
    postagem = get_object_or_404(Postagem, pk=postagem_id)

    if request.method == "POST":
        postagem.name = request.POST['name']
        postagem.release_year = request.POST['release_year']
        postagem.poster_url = request.POST['poster_url']
        postagem.save()
        return HttpResponseRedirect(
            reverse('postagens:detail', args=(postagem.id, )))

    context = {'postagem': postagem}
    return render(request, 'postagens/update.html', context)


def delete_postagem(request, postagem_id):
    postagem = get_object_or_404(Postagem, pk=postagem_id)

    if request.method == "POST":
        postagem.delete()
        return HttpResponseRedirect(reverse('Postagem:index'))

    context = {'postagem': postagem}
    return render(request, 'postagens/delete.html', context) """