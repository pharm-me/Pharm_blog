from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.urls import reverse_lazy
from django.views.generic import FormView

User=get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password1",
            "password2",
        ]

class SignUpView(FormView):
    template_name = "registration/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("index:index")

    def form_valid(self, form):
        form.save()

        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]

        user = authenticate(self.request, username=username, password=password)
        login(self.request, user)

        return super().form_valid(form)


