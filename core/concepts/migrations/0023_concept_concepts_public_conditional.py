# Generated by Django 3.2.8 on 2021-11-02 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concepts', '0022_auto_20211012_1333'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('is_latest_version', True), models.Q(('public_access', 'None'), _negated=True)), fields=['public_access'], name='concepts_public_conditional'),
        ),
    ]
