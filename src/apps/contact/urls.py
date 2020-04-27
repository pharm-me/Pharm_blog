from django.urls import path

from apps.contact.views import ContactView

from apps.contact.apps import ContactConfig

app_name = ContactConfig.name

urlpatterns = [
    path("", ContactView.as_view(), name="contact"),
]
