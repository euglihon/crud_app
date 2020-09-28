from django.urls import path
from .views import ArticleListView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView


urlpatterns = [
    path('', ArticleListView.as_view(), name='article_list_path'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name='article_update_path'),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail_path'),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete_path'),
]
