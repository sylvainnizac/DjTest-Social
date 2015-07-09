from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.views import logout
from django.views.generic import ListView
from django.db.models import Q
from itertools import chain
from social.models import MyWallMessage, OtherWallMessage, Profil

# Create your views here.

class List_Profils(ListView):
    """
    This class recover all Profils
    """
    model=Profil
    context_object_name="profils"
    template_name="social/profils.html"
    
    def get_queryset(self):
        return Profil.objects.filter(~Q(user=self.request.user.id))

class List_Messages(ListView):
    """
    This class allows to quickly call the article list. and return other useful data for the page
    """
    model=MyWallMessage
    context_object_name="messages"
    template_name="social/wall.html"
    paginate_by = 5

    def get_queryset(self):
        """Recover all Messages from the owner"""
        return MyWallMessage.objects.filter(owner=self.kwargs['owner'])

    def get_context_data(self, **kwargs):
        """recover and modify the context data to add the list of categories"""
        context = super(List_Messages, self).get_context_data(**kwargs)
        #add the new context data
        context['messages'] = list(chain(context['messages'], OtherWallMessage.objects.filter(receiver=self.kwargs['owner'])))
        return context
