# core/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from allauth.account.views import SignupView, LoginView


# Create your views here.
def index(request):
    return render(request, 'home.html')
@login_required
def profile(request):
    return render(request, 'account/profile.html')
