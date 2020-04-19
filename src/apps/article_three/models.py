from django.db import models as m


class ArticleContent(m.Model):
    article_three_content = m.TextField(null=True, blank=True)
