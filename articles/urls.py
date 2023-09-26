from . import views
from django.urls import path


app_name = 'articles'

urlpatterns = [
    # Define URL patterns for articles
    path('articles/', views.ArticleListView.as_view(), name='article_list'),
    path('articles/<slug:slug>/',
         views.ArticleDetailView.as_view(), name='article_detail'),

    # Define URL patterns for comments (optional)
    path('articles/<slug:slug>/comments/',
         views.CommentCreateView.as_view(), name='comment_create'),
]
