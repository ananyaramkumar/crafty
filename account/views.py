from django.db.models import Count
from django.views.generic import TemplateView
from crafty.models import Diy, Favorite

class ProfileView(TemplateView):

    template_name = "account/diys.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        diys =  Diy.objects.filter(creator=self.request.user).annotate(num_likes=Count('favorite'))
        for diy in diys:
            diy.favorite = diy.favorite_set.filter(user=self.request.user).count() == 0

        context['diys'] = diys

        return context

class FavoritesView(TemplateView):

    template_name = "account/favorites.html"

    def get_context_data(self, **kwargs):
        context = super(FavoritesView, self).get_context_data(**kwargs)
        favorites = Favorite.objects.filter(user=self.request.user)
        for favorite in favorites:
            favorite.diy.num_likes = favorite.diy.favorite_set.count()
            favorite.diy.favorite = favorite.diy.favorite_set.filter(user=self.request.user).count() == 0

        context['diys'] = favorites

        return context