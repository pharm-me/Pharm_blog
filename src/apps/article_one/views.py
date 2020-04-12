from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "article_one/article_one.html"
