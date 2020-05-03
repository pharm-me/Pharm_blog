from django.urls import path

from apps.article_one.views import ArticleView

urlpatterns = [
    path('article_one/<int:pk>/', ArticleView.as_view(), name='article_one'),
]
