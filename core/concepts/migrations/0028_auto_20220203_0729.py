# Generated by Django 3.2.8 on 2022-02-03 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concepts', '0027_remove_concept_concepts_is_acti_7190c6_idx'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('is_latest_version', True)), fields=['is_active'], name='concepts_all_for_count'),
        ),
        migrations.AddIndex(
            model_name='concept',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('is_latest_version', True)), fields=['-updated_at'], name='concepts_all_for_sort'),
        ),
    ]
