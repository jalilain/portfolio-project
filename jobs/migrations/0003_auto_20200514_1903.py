# Generated by Django 2.0.2 on 2020-05-14 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20200514_1902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='imageFun',
            new_name='image',
        ),
    ]
