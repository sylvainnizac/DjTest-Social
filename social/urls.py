# -*- coding: utf8 -*-
from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from social.views import List_Profils, List_Messages

urlpatterns = patterns('social.views',
    url(r'^$', auth_views.login, {"template_name" : "social/connect.html"}, name="accueil"),
    url(r'^deconnexion$', auth_views.logout, {"next_page" : "accueil"}, name="deconnexion"),
    url(r'^namebook$', List_Profils.as_view(), name="namebook"),
    url(r'^messages/(?P<owner>\d+)$', List_Messages.as_view(), name="wall"),
)
