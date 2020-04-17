from django.db import models as m


class ArticlePreview(m.Model):
    article = m.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Article Preview"

    def __str__(self):
        return "Article Preview"