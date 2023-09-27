from . import views
from django.urls import path


urlpatterns = [
    # URL patterns for viewing on views.py
    path('', views.ArticleList.as_view(), name='home'),
    path('<slug:slug>/', views.ArticleDetail.as_view(), name='article_detail'),
    # Likes section for URL viewing
    path('like/<slug:slug>', views.ArticlePostLike.as_view(), name='article_post_like'),
]
