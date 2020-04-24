from django.db import models as m
from datetime import datetime

class ArticleContent (m.Model):
    article_two_content = m.TextField(blank=True, null=True)
    article_two_time = m.DateField(default=datetime.utcnow())
