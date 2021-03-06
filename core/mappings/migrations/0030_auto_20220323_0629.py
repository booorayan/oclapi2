# Generated by Django 3.2.10 on 2022-03-23 06:29

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('mappings', '0029_mapping__index'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='mapping',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('id', django.db.models.expressions.F('versioned_object_id')), models.Q(('public_access', 'None'), _negated=True)), fields=['-updated_at'], name='mappings_vers_updated_idx'),
        ),
        migrations.AddIndex(
            model_name='mapping',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('id', django.db.models.expressions.F('versioned_object_id')), models.Q(('public_access', 'None'), _negated=True)), fields=['public_access'], name='mappings_ver_public_cond'),
        ),
        migrations.AddIndex(
            model_name='mapping',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('id', django.db.models.expressions.F('versioned_object_id'))), fields=['is_active'], name='mappings_ver_all_for_count'),
        ),
        migrations.AddIndex(
            model_name='mapping',
            index=models.Index(condition=models.Q(('is_active', True), ('retired', False), ('id', django.db.models.expressions.F('versioned_object_id'))), fields=['-updated_at'], name='mappings_ver_all_for_sort'),
        ),
    ]
