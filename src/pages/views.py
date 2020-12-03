from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic


# Create your views here.

def homePageView(request):
	template = loader.get_template('pages/index.html')
	return HttpResponse(template.render())
    

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'pages/signup.html'
