# Generated by Django 3.0.6 on 2020-05-13 14:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20200513_1637'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contributor',
            old_name='username',
            new_name='user',
        ),
    ]