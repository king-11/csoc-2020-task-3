# Generated by Django 3.0.6 on 2020-05-13 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_contributor'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contributor',
            old_name='person',
            new_name='username',
        ),
    ]
