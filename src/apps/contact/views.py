from django.views.generic import ListView, TemplateView


class ContactView(TemplateView):
    template_name = "contact/contact.html"
