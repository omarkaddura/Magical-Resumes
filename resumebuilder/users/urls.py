from django.urls import path, include
from . import views
from django.contrib.auth.models import User


urlpatterns = [
     path('', views.landing_page , name='landing_page'),
     path('accounts/', include("django.contrib.auth.urls")),
     path('register', views.register , name='register'),
]