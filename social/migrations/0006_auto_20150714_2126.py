# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0005_auto_20150712_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='receiver',
            field=models.ForeignKey(related_name='comm_receiver', verbose_name='Destinataire du commentaire', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='sender',
            field=models.ForeignKey(verbose_name='Rédacteur du commentaire', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='owner',
            field=models.ForeignKey(verbose_name='Rédacteur du message', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(related_name='mess_receiver', verbose_name='Mur où apparait le message', to=settings.AUTH_USER_MODEL),
        ),
    ]
