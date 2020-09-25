from django.views.generic import ListView
from .models import Article


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles_list'
    template_name = 'article_list.html'
