# Generated by Django 3.2.8 on 2021-12-16 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0012_remove_organization_internal_reference_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='overview',
            field=models.JSONField(default=dict),
        ),
    ]
