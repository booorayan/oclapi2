# Generated by Django 3.2.8 on 2021-11-10 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0024_mapping_mappings_public_conditional'),
    ]

    operations = [
        migrations.AddField(
            model_name='mapping',
            name='_counted',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
    ]
