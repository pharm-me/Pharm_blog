from django.views.generic import DetailView

from apps.index.models import ArticlePreview


class ArticleView(DetailView):
    template_name = "article_one/article_one.html"
    model = ArticlePreview
