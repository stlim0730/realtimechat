# Generated by Django 3.2.4 on 2021-07-09 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_alter_chat_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='date',
            new_name='chat_date',
        ),
    ]
