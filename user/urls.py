from django.conf.urls import url
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    # login page
    url(r'^login/$',LoginView.as_view(template_name='user/login.html'),
        name='login'),
    #path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),


    #for logout 
     url(r'^logout/$',views.logout_view, name='logout'),
]

app_name ='user'
