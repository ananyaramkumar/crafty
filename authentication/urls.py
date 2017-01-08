from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (
    password_reset, password_reset_confirm, password_reset_done)
from django.conf.urls import url
from . import views

app_name = 'authentication'

urlpatterns = [
    # login user
    url(r'^login/$',
        views.LoginView.as_view(), name='login'),

    # logout user
    url(r'^logout/$',
        login_required(views.LogoutView.as_view()), name='logout'),

    # register user
    url(r'^register/$',
        views.RegistrationView.as_view(), name='register'),

    # recover user
    url(r'^password/reset$', password_reset, name='reset_password'),

]