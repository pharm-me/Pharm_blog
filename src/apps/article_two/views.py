from django.views.generic import ListView

from apps.article_two.models import ArticleContent


class IndexView(ListView):
    template_name = "article_two/article_two.html"
    model = ArticleContent
