from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .models import Article
from django.urls import reverse_lazy


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles_list'
    template_name = 'article_list.html'


class ArticleDetailView(DeleteView):
    model = Article
    context_object_name = 'article'
    template_name = 'article_detail.html'


class ArticleUpdateView(UpdateView):
    model = Article
    context_object_name = 'article'
    fields = ['title', 'body']
    template_name = 'article_edit.html'


class ArticleDeleteView(DeleteView):
    model = Article
    context_object_name = 'article'
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list_path')


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = ['title', 'body', 'author']
    login_url = 'login' # path to login or registration page

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
