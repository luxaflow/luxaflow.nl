# Generated by Django 2.1.3 on 2018-11-29 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_skill_learning'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='software',
            new_name='other',
        ),
    ]
