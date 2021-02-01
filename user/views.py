from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse,logout
from django.contrib.auth.views import LogoutView

# Create your views here.
def logout_view(request):
    """logout"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

