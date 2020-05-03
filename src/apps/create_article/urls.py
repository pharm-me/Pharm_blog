from django.urls import path

from apps.create_article.views import ArticleCreateView

urlpatterns = [
    path('', ArticleCreateView.as_view(), name='create_article'),
]
