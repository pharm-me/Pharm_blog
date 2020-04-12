from django.urls import path

from apps.article_one.views import IndexView

from apps.article_one.apps import ArticleOneConfig

app_name = ArticleOneConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="article_one"),
]
