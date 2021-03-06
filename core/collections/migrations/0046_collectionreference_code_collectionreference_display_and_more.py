# Generated by Django 4.0.3 on 2022-04-19 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0045_alter_collection_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionreference',
            name='code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='collectionreference',
            name='display',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='collectionreference',
            name='filter',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='collectionreference',
            name='namespace',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='collectionreference',
            name='version',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
