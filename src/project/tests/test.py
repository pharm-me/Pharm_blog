from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve

from apps.index.views import IndexView

from apps.article_one.views import ArticleView

from apps.contact.views import ContactView


class TestUrls(SimpleTestCase):

    def test_index_url(self):
        url = reverse('index:index')
        self.assertEqual(resolve(url).func.view_class, IndexView)

    def test_article_one_url(self):
        url = reverse('article_one', args=[1])
        self.assertEqual(resolve(url).func.view_class, ArticleView)

    def test_contact_url(self):
        url = reverse('contact:contact')
        self.assertEqual(resolve(url).func.view_class, ContactView)

class TestViews(TestCase):
    def test_index_get(self):
        cli = Client()
        response = cli.get(reverse('index:index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index/index.html')


