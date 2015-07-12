# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_comment2'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentMyWall',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.TextField(verbose_name='Votre commentaire')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date du commentaire')),
                ('commentaire_visible', models.BooleanField(default=True)),
                ('message', models.ForeignKey(verbose_name='Message lié', to='social.MyWallMessage')),
                ('sender', models.ForeignKey(verbose_name='Rédacteur du commentaire', to='social.Profil')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CommentOtherWall',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('description', models.TextField(verbose_name='Votre commentaire')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date du commentaire')),
                ('commentaire_visible', models.BooleanField(default=True)),
                ('message', models.ForeignKey(verbose_name='Message lié', to='social.OtherWallMessage')),
                ('receiver', models.ForeignKey(to='social.Profil', related_name='comm_receiver', verbose_name='Destinataire du commentaire')),
                ('sender', models.ForeignKey(verbose_name='Rédacteur du commentaire', to='social.Profil')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='comment',
            name='message',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='sender',
        ),
        migrations.RemoveField(
            model_name='comment2',
            name='message',
        ),
        migrations.RemoveField(
            model_name='comment2',
            name='sender',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Comment2',
        ),
    ]
