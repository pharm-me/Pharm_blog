from django.contrib import admin
from django.contrib.admin import ModelAdmin

from apps.article_three.models import ArticleContent


@admin.register(ArticleContent)
class ArticleContentAdminModel(ModelAdmin):
    pass

