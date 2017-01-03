from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView
from django.contrib.auth.views import password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns = [
    url(r'^$',
        RedirectView.as_view(url=reverse_lazy('crafty:newsfeed'))),
    url(r'^admin/', admin.site.urls),
    url(r'^crafty/', include('crafty.urls', namespace="crafty")), 
    url(r'^profile/', include('account.urls', namespace="profile")), 
    url(r'^accounts/', include('authentication.urls', namespace="auth")),

    # reset confirmation
    url(r'^password/reset/done$',
        password_reset_done, name='password_reset_done'),

    url(r'^password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
        password_reset_confirm, name='password_reset_confirm'),

    url(r'^password/reset/complete/$',
        password_reset_complete, name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)