# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0002_auto_20150708_2148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('description', models.TextField(verbose_name='Votre commentaire')),
                ('date', models.DateTimeField(verbose_name='Date du commentaire', auto_now_add=True)),
                ('commentaire_visible', models.BooleanField(default=True)),
                ('message', models.ForeignKey(to='social.OtherWallMessage', verbose_name='Message lié')),
                ('sender', models.ForeignKey(to='social.Profil', verbose_name='Rédacteur du commentaire')),
            ],
        ),
    ]
