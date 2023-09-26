from django.conf.urls import url
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list.as_view, name="list"),
    path('about/', views.about),
    # url(r'^create/$', views.article_create, name="create"),
    # url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]
