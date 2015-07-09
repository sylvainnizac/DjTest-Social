# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Votre commentaire')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date du commentaire')),
                ('commentaire_visible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MyWallMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Votre message')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date du message')),
                ('message_visible', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(to='social.Profil', verbose_name='Rédacteur du message')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='OtherWallMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(verbose_name='Votre message')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date du message')),
                ('message_visible', models.BooleanField(default=True)),
                ('owner', models.ForeignKey(to='social.Profil', verbose_name='Rédacteur du message')),
                ('receiver', models.ForeignKey(to='social.Profil', related_name='receiver', verbose_name='Mur où apparait le message')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='message',
            field=models.ForeignKey(to='social.MyWallMessage', verbose_name='Message lié'),
        ),
        migrations.AddField(
            model_name='comment',
            name='sender',
            field=models.ForeignKey(to='social.Profil', verbose_name='Rédacteur du commentaire'),
        ),
    ]
