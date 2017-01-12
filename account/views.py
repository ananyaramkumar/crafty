from django.contrib.auth.models import User
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from crafty.models import Diy, Favorite
from .models import Follow

class ProfileView(TemplateView):

    template_name = "account/diys.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        user = User.objects.get(username=self.kwargs['username'])
        diys =  Diy.objects.filter(creator=user).annotate(num_likes=Count('favorite'))
        for diy in diys:
            diy.favorite = diy.favorite_set.filter(user=user).count() == 0

        context['diys'] = diys
        context['user'] = user
        context['follow'] = Follow.objects.filter(follower=self.request.user, followee=user).count() == 0

        return context

class FavoritesView(TemplateView):

    template_name = "account/favorites.html"

    def get_context_data(self, **kwargs):
        context = super(FavoritesView, self).get_context_data(**kwargs)
        user = User.objects.get(username=self.kwargs['username'])
        favorites = Favorite.objects.filter(user=user)
        for favorite in favorites:
            favorite.diy.num_likes = favorite.diy.favorite_set.count()
            favorite.diy.favorite = favorite.diy.favorite_set.filter(user=user).count() == 0

        context['diys'] = favorites
        context['user'] = user
        context['follow'] = Follow.objects.filter(follower=self.request.user, followee=user).count() == 0

        return context

def follow(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    Follow.objects.create(follower=request.user, followee=user)
    return HttpResponseRedirect(request.POST['url'])

def unfollow(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    Follow.objects.filter(follower=request.user, followee=user).delete()
    return HttpResponseRedirect(request.POST['url'])