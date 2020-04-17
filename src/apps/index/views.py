from django.shortcuts import render
from django.views.generic import TemplateView
from apps.index.models import ArticlePreview


class IndexView(TemplateView):
    template_name = "index/index.html"
    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data(**kwargs)
        info = ArticlePreview.objects.first()
        ctx = {"object": info}
        ctx.update(parent_ctx)
        return ctx
