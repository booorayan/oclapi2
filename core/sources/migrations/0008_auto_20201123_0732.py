# Generated by Django 3.0.9 on 2020-11-23 07:32

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sources', '0007_source_canonical_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='contact',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='content_type',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='copyright',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='identifier',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='jurisdiction',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='publisher',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='purpose',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='source',
            name='revision_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
