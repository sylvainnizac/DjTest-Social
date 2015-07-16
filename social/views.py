from itertools import chain
from django.shortcuts import redirect
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from social.models import Message, Profil, Comment
from social.forms import NewCom, NewMess

# Create your views here.

@login_required
class List_Profils(ListView):
    """
    This class recover all Profils
    """
    model=Profil
    context_object_name="profils"
    template_name="social/profils.html"
    
    def get_queryset(self):
        """Recover all profils except the logged user profil"""
        return Profil.objects.filter(~Q(user=self.request.user.id))
        
    def get_context_data(self, **kwargs):
        """Recover data specific to the logged user"""
        context = super(List_Profils, self).get_context_data(**kwargs)
        # add the new context data
        context['logged'] = Profil.objects.filter(user=self.request.user.id)
        return context

@login_required
class List_Messages(ListView):
    """
    This class allows to quickly call the article list. and return other useful data for the page
    """
    model=Message
    context_object_name="messages"
    template_name="social/wall.html"
    paginate_by = 5

    def get_queryset(self):
        """Recover all Messages from the owner"""
        return Message.objects.filter(Q(owner=self.kwargs['owner']) & Q(receiver=self.kwargs['owner']))

    def get_context_data(self, **kwargs):
        """recover and modify the context data to add the list of categories"""
        context = super(List_Messages, self).get_context_data(**kwargs)
        # add the new context data
        context['messages'] = list(chain(context['messages'], Message.objects.filter(Q(receiver=self.kwargs['owner']) & ~Q(owner=self.kwargs['owner']))))
        # sort all data by date, most recent first
        context['messages'].sort(key=lambda x: x.date, reverse=True)
        # add the owner data, in order to compare with the logged user
        context['owners'] = Profil.objects.filter(user=self.kwargs['owner'])
        # recover comments
        context['commentaires'] = Comment.objects.filter(sender_id=self.kwargs['owner'])
        # creating empty form
        formu = NewCom()
        context['formu'] = formu
        messu = NewMess()
        context['messu'] = messu
        return context

@login_required
def leave_comment(request, id_message):
    """path for new comment creation"""
    #POST is used to return form data
    if request.method == 'POST':
        sender = request.user.id
        form = NewCom(request.POST, sender=sender, id_message=id_message)
        if form.is_valid():
            form.save()
            return redirect('wall', request.user.id)

    return redirect('wall', request.user.id)

@login_required
def leave_message(request, receiver):
    """
    New wall message creation
    More comments in leave_comment
    """
    if request.method == 'POST':
        owner = request.user.id
        form = NewMess(request.POST, receiver=receiver, owner=owner)
        if form.is_valid():
            form.save()
            return redirect('wall', receiver)

    return redirect('wall', receiver)
