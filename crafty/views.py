from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views import generic
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import View, FormView, RedirectView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Diy

class ExplorerView(generic.ListView):
    template_name='crafty/index.html'
    context_object_name = 'diys'

    def get_queryset(self):
        return Diy.objects.all()

class NewsfeedView(generic.ListView):
    template_name='crafty/index.html'
    context_object_name = 'diys'

    def get_queryset(self):
        return Diy.objects.all()

class DetailView(generic.DetailView):
    model = Diy
    template_name = 'crafty/details.html'

class DiyCreate(CreateView):
    model = Diy
    fields = ['artist', 'title', 'genre', 'logo']

class DiyUpdate(UpdateView):
    model = Diy
    fields = ['artist', 'title', 'genre', 'logo']

class DiyDelete(DeleteView):
    model = Diy
    success_url = reverse_lazy('crafty:explorer')