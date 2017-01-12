from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse_lazy
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views import generic
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import View, FormView, RedirectView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect, get_object_or_404
from account.models import Follow
from .forms.diyForm import DiyForm
from .forms.instructionForm import InstructionForm
from .forms.materialForm import MaterialForm
from .models import Diy, Instruction, Material, Favorite

class ExplorerView(generic.ListView):
    template_name='crafty/index.html'
    context_object_name = 'diys'

    def get_queryset(self):
        queryset =  Diy.objects.all().annotate(num_likes=Count('favorite')).order_by('-num_likes')
        for item in queryset:
            item.favorite = item.favorite_set.filter(user=self.request.user).count() == 0
        return queryset

class NewsfeedView(generic.ListView):
    template_name='crafty/index.html'
    context_object_name = 'diys'

    def get_queryset(self):
        follows = Follow.objects.filter(follower=self.request.user)
        users = []
        for follow in follows:
            users.append(follow.followee)

        queryset =  Diy.objects.filter(creator__in=users).annotate(num_likes=Count('favorite')).order_by('-pk')
        for item in queryset:
            item.favorite = item.favorite_set.filter(user=self.request.user).count() == 0
        return queryset

class DetailView(generic.DetailView):
    model = Diy
    template_name = 'crafty/details.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        diy = Diy.objects.get(pk=int(self.kwargs['pk']))
        diy.materials = diy.material_set.all().order_by('pk')
        diy.hasMaterials = diy.material_set.count() > 0
        diy.instructions = diy.instruction_set.all().order_by('pk')
        diy.hasInstructions = diy.instruction_set.count() > 0
        context['diy'] = diy
        return context

class DiyCreate(CreateView):
    model = Diy
    form_class = DiyForm

    def form_valid(self, form):
        diy = form.save(commit=False)
        diy.creator = self.request.user
        diy.save()
        return HttpResponseRedirect(diy.get_absolute_url())

class DiyUpdate(UpdateView):
    model = Diy
    fields = ["title", "description", "skill_level", "category", "duration", "duration_units", "picture"]

class DiyDelete(DeleteView):
    model = Diy
    success_url = reverse_lazy('crafty:explorer')

class InstructionCreate(CreateView):
    model = Instruction
    form_class = InstructionForm

    def form_valid(self, form):
        instruction = form.save(commit=False)
        diy = Diy.objects.get(pk=int(self.kwargs['pk']))
        instruction.diy = diy
        instruction.save()
        return HttpResponseRedirect(diy.get_absolute_url())

class InstructionUpdate(UpdateView):
    model = Instruction
    fields = ['instruction', 'picture']

class InstructionDelete(DeleteView):
    model = Instruction

    def get_success_url(self):
        instruction = Instruction.objects.get(pk=int(self.kwargs['pk']))
        return instruction.diy.get_absolute_url()

class MaterialCreate(CreateView):
    model = Material
    form_class = MaterialForm

    def form_valid(self, form):
        material = form.save(commit=False)
        diy = Diy.objects.get(pk=int(self.kwargs['pk']))
        material.diy = diy
        material.save()
        return HttpResponseRedirect(diy.get_absolute_url())

class MaterialUpdate(UpdateView):
    model = Material
    fields = ['name', 'amount', 'units']

    def form_valid(self, form):
        material = form.save(commit=False)
        material.save()
        return HttpResponseRedirect(material.diy.get_absolute_url())

class MaterialDelete(DeleteView):
    model = Material

    def get_success_url(self):
        material = Material.objects.get(pk=int(self.kwargs['pk']))
        return material.diy.get_absolute_url()

def favorite(request, diy_id):
    diy = get_object_or_404(Diy, pk=diy_id)
    Favorite.objects.create(diy=diy, user=request.user)
    return HttpResponseRedirect(request.POST['url'])

def unfavorite(request, diy_id):
    diy = get_object_or_404(Diy, pk=diy_id)
    Favorite.objects.filter(diy=diy, user=request.user).delete()
    return HttpResponseRedirect(request.POST['url'])

class CopyrightView(TemplateView):
    template_name = "crafty/copywrite.html"