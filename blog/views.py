from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)

from .form import ArticleForm
from .models import Article


class ArticleCreateView(CreateView):
    template_name = 'articles/create.html'
    form_class = ArticleForm
    queryset = Article.objects.all() #<blog>/<modelname>_list.html

    # success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(self):
    #    return '/'


class ArticleListView(ListView):
    template_name = 'articles/list.html'
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = 'articles/detail.html'
    queryset = Article.objects.all()

    # allows me to use <int:id> in url
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)
