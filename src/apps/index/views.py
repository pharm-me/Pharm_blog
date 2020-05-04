from django.views.generic import ListView

from apps.index.models import ArticlePreview


class IndexView(ListView):
    template_name = "index/index.html"
    model = ArticlePreview
    context_object_name = "blog"
    ordering = ['-article_date']
