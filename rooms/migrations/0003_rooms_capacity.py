# Generated by Django 4.2.4 on 2023-08-29 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_alter_rooms_options_messages'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='capacity',
            field=models.PositiveIntegerField(default=0, max_length=20),
        ),
    ]