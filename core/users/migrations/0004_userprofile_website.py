# Generated by Django 3.0.9 on 2020-09-10 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200827_1240'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='website',
            field=models.TextField(blank=True, null=True),
        ),
    ]