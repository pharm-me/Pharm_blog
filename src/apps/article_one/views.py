from django.views.generic import ListView

from apps.article_one.models import ArticleContent


class IndexView(ListView):
    template_name = "article_one/article_one.html"
    model = ArticleContent
