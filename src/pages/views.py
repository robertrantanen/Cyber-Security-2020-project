from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic
from .models import Account


@login_required
def homePageView(request):
    try:
        account = Account.objects.get(user_id=request.user.id)
    except Account.DoesNotExist:
        account = None

    if not account:
        Account.objects.create(user=request.user, coins=1000000)

    accounts = Account.objects.exclude(user_id=request.user.id)
	
    return render(request, 'pages/index.html', {'accounts': accounts}) 


@login_required
def giftView(request):
	
	if request.method == 'POST':
		user = request.user
		to = User.objects.get(username=request.POST.get('to'))
		amount = int(request.POST.get('amount'))
 
		user.account.coins -= amount
		to.account.coins += amount
 
		user.account.save()
		to.account.save()
	
	return redirect('/')


@login_required
def addView(request):
	
	if request.method == 'POST':
		user = request.user
		user.account.coins += 1 
		user.account.save()
	
	return redirect('/')

@login_required
def prizeView(request):
	return render(request, 'pages/prize.html')

    

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = 'http://127.0.0.1:8000/'
    template_name = 'pages/signup.html'
