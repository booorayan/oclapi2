# Generated by Django 3.1.12 on 2021-07-20 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concepts', '0015_auto_20210716_1353'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='localizedtext',
            index=models.Index(fields=['name'], name='localized_t_name_9b0703_idx'),
        ),
        migrations.AddIndex(
            model_name='localizedtext',
            index=models.Index(fields=['type'], name='localized_t_type_1a9d65_idx'),
        ),
        migrations.AddIndex(
            model_name='localizedtext',
            index=models.Index(fields=['locale'], name='localized_t_locale_d5efa2_idx'),
        ),
        migrations.AddIndex(
            model_name='localizedtext',
            index=models.Index(fields=['locale_preferred'], name='localized_t_locale__f23c8e_idx'),
        ),
    ]
