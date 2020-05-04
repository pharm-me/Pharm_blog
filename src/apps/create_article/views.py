from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView

from apps.index.models import ArticlePreview


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = ArticlePreview
    template_name = "create_article/create_article.html"
    fields = ['article_title', 'article_text','image']
    success_url = reverse_lazy('index:index')
