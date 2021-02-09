from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.views import LogoutView

# Create your views here.
def logout_view(request):
    """logout"""
    LogoutView(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

