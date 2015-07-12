from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profil(models.Model):
    """
    User profile, juste a little modification from standard one
    """
    HOMME = "H"
    FEMME = "F"
    AUTRE = "X"
    
    SEXE = (
    (HOMME, "Homme"),
    (FEMME, "Femme"),
    (AUTRE, "Non défini"),
    )

    user = models.OneToOneField(User, unique = True)  # OneToOne to model User
    sexe = models.CharField(max_length=1, choices=SEXE, default=AUTRE)
    avatar = models.ImageField(default="defaut.png", upload_to="avatars/")

    def __str__(self):
        return self.user.username

class Message(models.Model):
    """
    Abstract Message model
    """
    owner = models.ForeignKey('Profil', verbose_name="Rédacteur du message")
    message = models.TextField(verbose_name="Votre message")
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date du message")
    message_visible = models.BooleanField(default = True)
    
    class Meta:
        abstract = True

class MyWallMessage(Message):
    """
    All messages written on your wall
    """
    def __str__(self):
        return "{}".format(self.pk)

class OtherWallMessage(Message):
    """
    All messages writen on another wall
    """
    receiver = models.ForeignKey('Profil', verbose_name="Mur où apparait le message", related_name="receiver")
    
    def __str__(self):
        return "{}".format(self.pk)

class Comment(models.Model):
    """
    Table of comments
    """
    sender = models.ForeignKey('Profil', verbose_name="Rédacteur du commentaire")
    description = models.TextField(verbose_name="Votre commentaire")
    date = models.DateTimeField(auto_now_add=True, auto_now=False, verbose_name="Date du commentaire")
    commentaire_visible = models.BooleanField(default = True)

    class Meta:
        abstract = True

class CommentMyWall(Comment):
    """
    All comments linked to MyWallMessage
    """
    message = models.ForeignKey('MyWallMessage', verbose_name="Message lié")

    def __str__(self):
        return "{}".format(self.pk)

class CommentOtherWall(Comment):
    """
    All Comments linked to OtherWallMessage
    """
    message = models.ForeignKey('OtherWallMessage', verbose_name="Message lié")
    receiver = models.ForeignKey('Profil', verbose_name="Destinataire du commentaire", related_name="comm_receiver")

    def __str__(self):
        return "{}".format(self.pk)