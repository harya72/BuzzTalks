# Generated by Django 4.2.4 on 2023-08-29 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0005_myroom'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myroom',
            options={'verbose_name': 'Room'},
        ),
        migrations.RemoveField(
            model_name='myroom',
            name='rooms',
        ),
        migrations.AddField(
            model_name='myroom',
            name='name',
            field=models.CharField(default=None, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myroom',
            name='slug',
            field=models.SlugField(default=1, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='messages',
            name='room',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='rooms.myroom'),
        ),
        migrations.DeleteModel(
            name='Rooms',
        ),
    ]
