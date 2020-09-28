from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleCreateView


urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list_path'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_update_path'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail_path'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete_path'),
    path('new_article/', ArticleCreateView.as_view(), name='article_new-article_path'),
]
