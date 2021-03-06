# Generated by Django 3.1.12 on 2021-07-16 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0007_auto_20210326_1027'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='organization',
            index=models.Index(fields=['mnemonic'], name='organizatio_mnemoni_4ee8c7_idx'),
        ),
        migrations.AddIndex(
            model_name='organization',
            index=models.Index(fields=['uri'], name='organizatio_uri_227cb4_idx'),
        ),
        migrations.AddIndex(
            model_name='organization',
            index=models.Index(fields=['-updated_at'], name='organizatio_updated_9712da_idx'),
        ),
        migrations.AddIndex(
            model_name='organization',
            index=models.Index(fields=['-created_at'], name='organizatio_created_7f4ee3_idx'),
        ),
    ]
