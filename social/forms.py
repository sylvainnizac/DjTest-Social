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
        # On passe la foreign_key en paramètre à partir de la view
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
        # On ajoute à l'instance la foreignkey
        self.instance.sender = self.sender[0]
        self.instance.message = self.message[0]
        self.instance.receiver = self.receiver
        # On peut maintenant sauver
        super(NewCom, self).save(commit)

    class Meta:
        model = Comment
        fields = ('description', )