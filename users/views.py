from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import reverse
from django.contrib.auth.views import auth_login
from .forms import SignupFrom
User = get_user_model()

class SignUp(generic.CreateView):
    form_class = SignupFrom
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'