from django.db import models as m
from datetime import datetime

class ArticleContent (m.Model):
    article_one_content = m.TextField(null=True, blank=True)
    article_one_time = m.DateField(default=datetime.utcnow())

