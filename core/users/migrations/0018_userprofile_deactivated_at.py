# Generated by Django 3.2.8 on 2021-12-27 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_remove_userprofile_internal_reference_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='deactivated_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
