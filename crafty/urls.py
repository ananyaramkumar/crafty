from django.contrib.auth.decorators import login_required
from django.conf.urls import url
from . import views

app_name = 'crafty'

urlpatterns = [

    # crafty home page, "go to views"
    url(r'^explorer/$', login_required(views.ExplorerView.as_view()), name='explorer'),

        # crafty home page, "go to views"
    url(r'^newsfeed/$', login_required(views.NewsfeedView.as_view()), name='newsfeed'),

    # diy details page, "diy, display songs & everything"
    # crafty/2/
    url(r'^(?P<pk>[0-9]+)/$',
        login_required(views.DetailView.as_view()), name='detail'),

    # crafty/diy/add
    url(r'^diy/add/$',
        login_required(views.DiyCreate.as_view()), name='diy-add'),

    # crafty/diy/update/2/
    url(r'^diy/update/(?P<pk>[0-9]+)/$',
      login_required(views.DiyUpdate.as_view()), name='diy-update'),

    # crafty/diy/delete/2/
    url(r'^diy/delete/(?P<pk>[0-9]+)/$',
      login_required(views.DiyDelete.as_view()), name='diy-delete'),

]