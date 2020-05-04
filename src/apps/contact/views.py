from django.views.generic import ListView
from django.views.generic import TemplateView


class ContactView(TemplateView):
    template_name = "contact/contact.html"
