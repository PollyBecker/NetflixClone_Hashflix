# Generated by Django 4.0.2 on 2022-02-14 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filme',
            old_name='views',
            new_name='visualizados',
        ),
    ]