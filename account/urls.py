from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views

app_name = 'account'

urlpatterns = [
    url(r'^personal/(?P<username>.+)/$',
        login_required(views.ProfileView.as_view()), name='index'),

    url(r'^favorites/(?P<username>.+)/$',
        login_required(views.FavoritesView.as_view()), name='favorites'),

    # crafty/follow/2/
    url(r'^follow/(?P<user_id>[0-9]+)/$',
      login_required(views.follow), name='follow'),

    # crafty/follow/2/
    url(r'^unfollow/(?P<user_id>[0-9]+)/$',
      login_required(views.unfollow), name='unfollow'),
]