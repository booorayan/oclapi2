# Generated by Django 3.2.8 on 2022-02-04 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0036_auto_20220204_0851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collectionreference',
            old_name='_concepts',
            new_name='concepts',
        ),
        migrations.RenameField(
            model_name='collectionreference',
            old_name='_mappings',
            new_name='mappings',
        ),
    ]
