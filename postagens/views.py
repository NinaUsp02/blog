from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponse
from .temp_data import postagem_data
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Postagem, Review, List
from django.views import generic
from .forms import PostagemForm, ReviewForm


class PostagemListView(generic.ListView):
    model = Postagem
    template_name = 'postagens/index.html'

class PostagemDetailView(generic.DetailView):
    model = Postagem
    template_name = 'postagens/detail.html'
    context_object_name = 'postagem'
    def get_object(self, queryset=None):
        return get_object_or_404(Postagem, pk=self.kwargs.get('pk'))
    
def search_postagens(request):
    context = {}
    if request.GET.get("query", False):
        search_term = request.GET["query"].lower()
        postagem_list = Postagem.objects.filter(name__icontains=search_term)
        context = {"postagem_list": postagem_list}
    return render(request, "postagens/search.html", context)

class PostagemCreateView(generic.CreateView):
    model = Postagem
    form_class = PostagemForm
    template_name = 'postagens/create.html'
    success_url = reverse_lazy('postagens:index')

class PostagemUpdateView(generic.UpdateView):
    model = Postagem
    form_class = PostagemForm
    template_name = 'postagens/update.html'
    success_url = reverse_lazy('postagens:index')

class PostagemDeleteView(generic.DeleteView):
    model = Postagem
    template_name = 'postagens/delete.html'
    success_url = reverse_lazy('postagens:index')

def create_review(request, postagem_id):
    postagem = get_object_or_404(Postagem, pk=postagem_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review_author = form.cleaned_data['author']
            review_text = form.cleaned_data['text']
            review = Review(author=review_author,
                            text=review_text,
                            postagem=postagem)
            review.save()
            return HttpResponseRedirect(
                reverse('postagens:detail', args=(postagem_id, )))
    else:
        form = ReviewForm()
    context = {'form': form, 'postagem': postagem}
    return render(request, 'postagens/review.html', context)


class ListListView(generic.ListView):
    model = List
    template_name = 'postagens/lists.html'


class ListCreateView(generic.CreateView):
    model = List
    template_name = 'postagens/create_list.html'
    fields = ['name', 'author', 'postagens']
    success_url = reverse_lazy('postagens:lists')