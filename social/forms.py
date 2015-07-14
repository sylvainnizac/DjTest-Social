# -*- coding: utf8 -*-
from django import forms
from social.models import Comment, Profil, Message


class ConnectProfil(forms.Form):
    """
    formulaire de connexion minimal
    """
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class NewCom(forms.ModelForm):
    """form to add a comment, save is redefined to include the foreign keys"""
    def __init__(self, *args, **kwargs):
        # extracting data
        k = 'sender'
        if k in kwargs:
            self.sender = Profil.objects.filter(id=kwargs.pop('sender'))
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
        self.instance.sender = self.sender[0]
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
            self.owner = Profil.objects.filter(id=kwargs.pop('owner'))
        k ='receiver'
        if k in kwargs:
            self.receiver = Profil.objects.filter(id=kwargs.pop('receiver'))
        super(NewMess, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        # On sauve sans faire la requête SQL (commit=False) pour
        # pouvoir ajouter à l'instance la foreignkey
        super(NewMess, self).save(commit=False)
        # adding foreignkeys
        self.instance.owner = self.owner[0]
        self.instance.receiver = self.receiver[0]
        # now saving
        super(NewMess, self).save(commit)

    class Meta:
        model = Message
        fields = ('message', )
        widgets = {'message': forms.Textarea(attrs={'placeholder': 'Votre message', 'class' : 'id_description'})}
        labels = {'message' : ""}