# -*- coding: utf8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as OriginalUserAdmin
from django.contrib.auth.models import User
from social.models import Profil, MyWallMessage, Comment, OtherWallMessage

class ProfilInline(admin.StackedInline):
    """"""
    model = Profil
    can_delete = False
    
class ProfilAdmin(OriginalUserAdmin):
    """
    Extended version of the UserAdmin class
    """
    inlines = [ProfilInline, ]
    
class ProfilAdmin2(admin.ModelAdmin):
    list_display   = ('user', 'sexe', 'avatar', )

class MessageAdmin(admin.ModelAdmin):
    list_display   = ('owner', 'date', 'apercu_contenu', 'message_visible',)
    list_filter    = ('owner','date',)
    date_hierarchy = 'date'
    ordering       = ('-date', )
    search_fields  = ('owner', 'date')
    
        # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (auteur)
       ('Général',
       {'fields': ('owner',)}),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article',
        { 'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
        'fields': ('message',)}),
    )
    
    def apercu_contenu(self, article):
        """ 
        Retourne les 40 premiers caractères du contenu de l'article. S'il
        y a plus de 40 caractères, il faut ajouter des points de suspension. 
        """
        text = article.message[0:40]
        if len(article.message) > 40:
            return '%s…' % text
        else:
            return text

    # En-tête de notre colonne
    apercu_contenu.short_description = 'Aperçu du contenu'

class OtherWallMessageAdmin(admin.ModelAdmin):
    list_display   = ('owner', 'receiver', 'date', 'apercu_contenu', 'message_visible',)
    list_filter    = ('owner','date', 'receiver', )
    date_hierarchy = 'date'
    ordering       = ('-date', 'receiver', )
    search_fields  = ('owner', 'date', 'receiver',)
    
        # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (auteur)
       ('Général',
       {'fields': ('owner', 'receiver')}),
        # Fieldset 2 : contenu de l'article
        ('Contenu de l\'article',
        { 'description': 'Le formulaire accepte les balises HTML. Utilisez-les à bon escient !',
        'fields': ('message',)}),
    )
    
    def apercu_contenu(self, article):
        """ 
        Retourne les 40 premiers caractères du contenu de l'article. S'il
        y a plus de 40 caractères, il faut ajouter des points de suspension. 
        """
        text = article.message[0:40]
        if len(article.message) > 40:
            return '%s…' % text
        else:
            return text

    # En-tête de notre colonne
    apercu_contenu.short_description = 'Aperçu du contenu'

class CommentAdmin(admin.ModelAdmin):
    list_display   = ('sender', 'message', 'apercu_description', 'date', 'commentaire_visible',)
    list_filter    = ('sender', 'message', )
    date_hierarchy = 'date'
    ordering       = ('-date', )
    search_fields  = ('sender', 'message', 'date', )
    
        # Configuration du formulaire d'édition
    fieldsets = (
        # Fieldset 1 : meta-info (message lié au commentaire)
       ('Général',
       {'fields': ('sender', 'message'), }),
        # Fieldset 2 : contenu de l'article
        ('Commentaire',
        { 'description': 'Le formulaire n\'accepte pas les balises HTML.',
        'fields': ('description', )}),
        # Fieldset 3 : modération
        ('Modération',
        { 'fields': ('commentaire_visible', )}),
    )
    
    def apercu_description(self, commentaire):
        """ 
        Retourne les 40 premiers caractères du contenu du commentaire. S'il
        y a plus de 40 caractères, il faut ajouter des points de suspension. 
        """
        text = commentaire.description[0:40]
        if len(commentaire.description) > 40:
            return '%s…' % text
        else:
            return text

    # En-tête de notre colonne
    apercu_description.short_description = 'Aperçu du commentaire'

# Register your models here.
try:
    admin.site.unregister(User)
finally:
    admin.site.register(User, ProfilAdmin)

admin.site.register(MyWallMessage, MessageAdmin)
admin.site.register(OtherWallMessage, OtherWallMessageAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Profil, ProfilAdmin2)
