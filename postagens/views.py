from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from .models import Postagem, Comment, Category
from django.views import generic
from .forms import PostagemForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


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


class PostagemCreateView(LoginRequiredMixin, generic.CreateView):
    model = Postagem
    form_class = PostagemForm
    template_name = 'postagens/create.html'
    success_url = reverse_lazy('postagens:index')

class PostagemUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Postagem
    form_class = PostagemForm
    template_name = 'postagens/update.html'
    success_url = reverse_lazy('postagens:index')

class PostagemDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Postagem
    template_name = 'postagens/delete.html'
    success_url = reverse_lazy('postagens:index')

@login_required
def create_comment(request, postagem_id):
    postagem = get_object_or_404(Postagem, pk=postagem_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = request.user
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            postagem=postagem)
            comment.save()
            return HttpResponseRedirect(
                reverse('postagens:detail', args=(postagem_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'postagem': postagem}
    return render(request, 'postagens/comment.html', context)


def list_categories(request):
    category_list = Category.objects.all()
    context = {'category_list':category_list}
    return render(request, "postagens/list_categories.html", context)

def individual_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    postagens = category.postagens.all()
    context = {'category': category, 'postagens': postagens}
    return render(request, 'postagens/individual_category.html', context)



