# Generated by Django 3.2.10 on 2022-04-06 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0043_expansion_is_processing'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='concepts',
        ),
        migrations.RemoveField(
            model_name='collection',
            name='mappings',
        ),
    ]
