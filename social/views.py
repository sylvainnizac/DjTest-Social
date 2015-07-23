from itertools import chain
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from social.models import Message, Profil, Comment
from social.forms import NewCom, NewMess, ConnectProfil, CreateProfil


# Create your views here.

def connexion(request):
    """
    User connection
    """
    error = False
    if request.method == "POST":
        form = ConnectProfil(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # check username/password validity
            if user:  # If OK, i.e. not None
                login(request, user)  # connecting
                if request.user.is_superuser:
                    error = True
                    return redirect('deconnexion')

            else: # wrong user/pwd error
                error = True
    else:
        form = ConnectProfil()

    return render(request, 'social/connect.html', locals())

def user_creation(request):
    """
    User creation
    """
    error = False
    if request.method == "POST":
        form = CreateProfil(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            prenom = form.cleaned_data["prenom"]
            nom = form.cleaned_data["nom"]
            sexe = form.cleaned_data["sexe"]
            email = form.cleaned_data["email"]
            avatar = form.cleaned_data["avatar"]
            password = form.cleaned_data["password"]
            confirm_password = form.cleaned_data["confirm_password"]

            if password != confirm_password:
                error = True
                msg = "Veuillez vérifier le mot de passe."
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=prenom, last_name=nom)
                user.save()
                # to be implemented, non-unique user error catch
                profil = Profil(user.id, sexe, avatar)
                profil.save()
                return redirect('accueil')
    else:
        form = CreateProfil()

    return render(request, 'social/creation.html', locals())

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
