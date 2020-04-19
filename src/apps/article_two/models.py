from django.db import models as m

class ArticleContent (m.Model):
    article_two_content = m.TextField(blank=True, null=True)
