from django.views.generic import TemplateView

class ProfileView(TemplateView):

    template_name = "account/index.html"

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context