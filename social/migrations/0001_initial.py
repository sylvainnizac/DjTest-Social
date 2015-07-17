# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('description', models.TextField(verbose_name='Votre commentaire')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date du commentaire')),
                ('commentaire_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('message', models.TextField(verbose_name='Votre message')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date du message')),
                ('message_visible', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Rédacteur du message')),
                ('receiver', models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Mur où apparait le message', related_name='mess_receiver')),
            ],
        ),
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('sexe', models.CharField(max_length=1, choices=[('H', 'Homme'), ('F', 'Femme'), ('X', 'Non défini')], default='X')),
                ('avatar', models.ImageField(default='defaut.png', upload_to='avatars/')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.ForeignKey(to='social.Message', verbose_name='Message lié'),
        ),
        migrations.AddField(
            model_name='comment',
            name='receiver',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Destinataire du commentaire', related_name='comm_receiver'),
        ),
        migrations.AddField(
            model_name='comment',
            name='sender',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Rédacteur du commentaire'),
        ),
    ]
