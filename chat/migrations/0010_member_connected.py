# Generated by Django 3.2.4 on 2021-07-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0009_alter_chat_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='connected',
            field=models.BooleanField(default=False),
        ),
    ]
