from django.contrib import admin
from django.contrib.admin import ModelAdmin
from apps.index.models import ArticlePreview

@admin.register(ArticlePreview)
class ArticlePreviewAdminModel(ModelAdmin):
    pass

