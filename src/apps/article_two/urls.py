from django.urls import path

from apps.article_two.views import IndexView

from apps.article_two.apps import ArticleTwoConfig

app_name = ArticleTwoConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="article_two"),
]
