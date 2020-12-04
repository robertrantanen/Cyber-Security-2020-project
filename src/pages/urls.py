from django.urls import path

from .views import homePageView
from .views import SignUpView
from .views import giftView
from .views import addView

urlpatterns = [
    path('', homePageView, name='home'),
    path('gift/', giftView, name='gift'),
    path('add/', addView, name='add'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
