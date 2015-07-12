# -*- coding: utf8 -*-
from django import forms
from social.models import Comment


class ConnectProfil(forms.Form):
    """
    formulaire de connexion minimal
    """
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

class NewCom(forms.ModelForm):
    """really, a description?"""
    def __init__(self, *args, **kwargs):
        # On passe la foreign_key en paramètre à partir de la view
        k = 'article'
        if k in kwargs:
            self.article = kwargs.pop('article')
        super(NewCom, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        # On sauve sans faire la requête SQL (commit=False) pour
        # pouvoir ajouter à l'instance la foreignkey
        super(NewCom, self).save(commit=False)
        # On ajoute à l'instance la foreignkey
        self.instance.article = self.article
        # On peut maintenant sauver
        super(NewCom, self).save(commit)

    class Meta:
        model = Comment
        fields = ('description', )