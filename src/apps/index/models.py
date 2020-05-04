from django.db import models as m


class ArticlePreview(m.Model):
    article_title = m.TextField(null=True, blank=True)
    article_text = m.TextField(null=True, blank=True)
    article_date = m.DateTimeField(auto_now=True)
    image = m.ImageField(null=True, blank=True)
    class Meta:
        verbose_name_plural = "Article"

    def __str__(self):
        return f'{self.article_title}'
