from django.views.generic import TemplateView

from apps.article_two.models import ArticleContent


class IndexView(TemplateView):
    template_name = "article_two/article_two.html"

    def get_context_data(self, **kwargs):
        parent_ctx = super().get_context_data(**kwargs)
        info = ArticleContent.objects.first()
        ctx = {"object": info}
        ctx.update(parent_ctx)
        return ctx
