# Generated by Django 3.1.12 on 2021-07-16 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0008_auto_20210716_1341'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='organization',
            index=models.Index(fields=['is_active'], name='organizatio_is_acti_bdc355_idx'),
        ),
    ]
