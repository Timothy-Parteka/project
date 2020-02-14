# create a view which uses the built-in
# UserCreationForm and generic CreateView
# for the signup
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    # reverse_lazy directs the user to the login page
    # upon a successful registration
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
