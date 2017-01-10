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

    # crafty/instruction/add/2/
    url(r'^instruction/add/(?P<pk>[0-9]+)/$',
        login_required(views.InstructionCreate.as_view()), name='instruction-add'),

    # crafty/instruction/update/2/
    url(r'^instruction/update/(?P<pk>[0-9]+)/$',
      login_required(views.InstructionUpdate.as_view()), name='instruction-update'),

    # crafty/instruction/delete/2/
    url(r'^instruction/delete/(?P<pk>[0-9]+)/$',
      login_required(views.InstructionDelete.as_view()), name='instruction-delete'),

    # crafty/material/add/2/
    url(r'^material/add/(?P<pk>[0-9]+)/$',
        login_required(views.MaterialCreate.as_view()), name='material-add'),

    # crafty/material/update/2/
    url(r'^material/update/(?P<pk>[0-9]+)/$',
      login_required(views.MaterialUpdate.as_view()), name='material-update'),

    # crafty/material/delete/2/
    url(r'^material/delete/(?P<pk>[0-9]+)/$',
      login_required(views.MaterialDelete.as_view()), name='material-delete'),

    # crafty/favorite/2/
    url(r'^favorite/(?P<diy_id>[0-9]+)/$',
      login_required(views.favorite), name='favorite'),

    # crafty/unfavorite/2/
    url(r'^unfavorite/(?P<diy_id>[0-9]+)/$',
      login_required(views.unfavorite), name='unfavorite'),

]