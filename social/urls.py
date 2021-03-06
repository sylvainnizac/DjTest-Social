# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from social.views import List_Profils, List_Messages


urlpatterns = patterns('social.views',
    url(r'^$', 'connexion', name="accueil"),
    url(r'^creation$', 'user_creation', name="creation"),
    url(r'^deconnexion$', auth_views.logout, {"next_page" : "accueil"}, name="deconnexion"),
    url(r'^namebook$', login_required(List_Profils.as_view()), name="namebook"),
    url(r'^messages/(?P<owner>\d+)$', login_required(List_Messages.as_view()), name="wall"),
    url(r'^comms/(?P<id_message>\d+)$', 'leave_comment', name="comm"),
    url(r'^mess/(?P<receiver>\d+)$', 'leave_message', name="mess"),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
