# -*- coding: utf8 -*-
from django import forms
from social.models import Comment, Profil, Message


class ConnectProfil(forms.Form):
    """
    formulaire de connexion minimal
    """
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class CreateProfil(forms.ModelForm):
    """
    Profil creation form
    """
    username = forms.CharField(label="Nom d'utilisateur", max_length=30, required=True)
    prenom = forms.CharField(label="Prénom", max_length=30)
    nom = forms.CharField(label="Nom", max_length=30)
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput, required=True)
    confirm_password = forms.CharField(label="Confirmer mot de passe", widget=forms.PasswordInput, required=True)

    class Meta:
        model = Profil
        exclude = ('user', )
        fields = ('username', 'prenom', 'nom', 'sexe', 'email', 'avatar', 'password', 'confirm_password')



class NewCom(forms.ModelForm):
    """form to add a comment, save is redefined to include the foreign keys"""
    def __init__(self, *args, **kwargs):
        # extracting data
        k = 'sender'
        if k in kwargs:
            self.sender = Profil.objects.filter(user_id=kwargs.pop('sender'))
            self.sender = self.sender[0]
        k = 'id_message'
        if k in kwargs:
            self.message = Message.objects.filter(id=kwargs.pop('id_message'))
            temp = self.message[0]
            self.receiver = temp.receiver
        super(NewCom, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        # On sauve sans faire la requête SQL (commit=False) pour
        # pouvoir ajouter à l'instance la foreignkey
        super(NewCom, self).save(commit=False)
        # On ajoute à l'instance les foreignkeys
        self.instance.sender = self.sender.user
        self.instance.message = self.message[0]
        self.instance.receiver = self.receiver
        # On peut maintenant sauver
        super(NewCom, self).save(commit)

    class Meta:
        model = Comment
        fields = ('description', )
        widgets = {'description': forms.Textarea(attrs={'placeholder': 'Votre commentaire', 'class' : 'id_description'})}
        labels = {'description' : ""}

class NewMess(forms.ModelForm):
    """form to add a new message on your wall or another wall"""
    def __init__(self, *args, **kwargs):
        # extracting parameters data
        k ='owner'
        if k in kwargs:
            self.owner = Profil.objects.filter(user_id=kwargs.pop('owner'))
            self.owner = self.owner[0]
        k ='receiver'
        if k in kwargs:
            self.receiver = Profil.objects.filter(user_id=kwargs.pop('receiver'))
            self.receiver = self.receiver[0]
        super(NewMess, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        # On sauve sans faire la requête SQL (commit=False) pour
        # pouvoir ajouter à l'instance la foreignkey
        super(NewMess, self).save(commit=False)
        # adding foreignkeys
        self.instance.owner = self.owner.user
        self.instance.receiver = self.receiver.user
        # now saving
        super(NewMess, self).save(commit)

    class Meta:
        model = Message
        fields = ('message', )
        widgets = {'message': forms.Textarea(attrs={'placeholder': 'Votre message', 'class' : 'id_description'})}
        labels = {'message' : ""}