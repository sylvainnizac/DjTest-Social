# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0004_auto_20150712_1459'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('description', models.TextField(verbose_name='Votre commentaire')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date du commentaire')),
                ('commentaire_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('message', models.TextField(verbose_name='Votre message')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date du message')),
                ('message_visible', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(to='social.Profil', verbose_name='Rédacteur du message')),
                ('receiver', models.ForeignKey(to='social.Profil', verbose_name='Mur où apparait le message', related_name='mess_receiver')),
            ],
        ),
        migrations.RemoveField(
            model_name='commentmywall',
            name='message',
        ),
        migrations.RemoveField(
            model_name='commentmywall',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='commentotherwall',
            name='message',
        ),
        migrations.RemoveField(
            model_name='commentotherwall',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='commentotherwall',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='mywallmessage',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='otherwallmessage',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='otherwallmessage',
            name='receiver',
        ),
        migrations.DeleteModel(
            name='CommentMyWall',
        ),
        migrations.DeleteModel(
            name='CommentOtherWall',
        ),
        migrations.DeleteModel(
            name='MyWallMessage',
        ),
        migrations.DeleteModel(
            name='OtherWallMessage',
        ),
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.ForeignKey(to='social.Message', verbose_name='Message lié'),
        ),
        migrations.AddField(
            model_name='comment',
            name='receiver',
            field=models.ForeignKey(to='social.Profil', verbose_name='Destinataire du commentaire', related_name='comm_receiver'),
        ),
        migrations.AddField(
            model_name='comment',
            name='sender',
            field=models.ForeignKey(to='social.Profil', verbose_name='Rédacteur du commentaire'),
        ),
    ]
