from django.urls import path

from apps.article_three.views import IndexView

from apps.article_three.apps import ArticleThreeConfig

app_name = ArticleThreeConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="article_three"),
]
