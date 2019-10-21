# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-10-17 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wall', '0003_event_messages_new_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='wall.New_User'),
        ),
        migrations.AlterField(
            model_name='event',
            name='rsvp',
            field=models.ManyToManyField(related_name='user', to='wall.New_User'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='message', to='wall.New_User'),
        ),
    ]