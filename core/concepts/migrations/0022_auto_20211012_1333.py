# Generated by Django 3.2.7 on 2021-10-12 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concepts', '0021_auto_20211012_1107'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='concept',
            name='concepts_is_acti_ec40a2_idx',
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('is_latest_version', True), models.Q(('public_access', 'None'), _negated=True)), fields=['-updated_at'], name='concepts_updated_6490d8_idx'),
        ),
    ]
