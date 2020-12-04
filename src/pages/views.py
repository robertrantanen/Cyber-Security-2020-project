from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic


@login_required
def homePageView(request):
	return render(request, 'pages/index.html')
    

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = 'http://127.0.0.1:8000/'
    template_name = 'pages/signup.html'
