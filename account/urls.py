from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views

app_name = 'account'

urlpatterns = [
    # logout user
    url(r'^(?P<pk>[0-9]+)/$',
        login_required(views.ProfileView.as_view()), name='index'),
]