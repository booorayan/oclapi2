# Generated by Django 3.1.9 on 2021-07-28 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0025_auto_20210720_1000'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='autoexpand',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='collection',
            name='autoexpand_head',
            field=models.BooleanField(default=True),
        ),
    ]