from django.urls import path

from .views import homePageView
from .views import SignUpView

urlpatterns = [
    path('', homePageView, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
