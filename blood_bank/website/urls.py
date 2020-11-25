from django.urls import path
from . import views
from django.contrib.auth import login
from django.contrib.auth.views import LoginView



urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('preregister/', views.preregister, name='preregister'),
    path('request-blood/', views.requestblood, name='request-blood'),
    path('sign-in/', LoginView.as_view(template_name='website/sign-in.html'), name='sign-in'),
    path('sign-up/', views.signup, name='sign-up'),
]

