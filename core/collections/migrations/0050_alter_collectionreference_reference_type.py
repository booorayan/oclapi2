# Generated by Django 4.0.3 on 2022-05-02 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collections', '0049_auto_20220502_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionreference',
            name='reference_type',
            field=models.CharField(choices=[('concepts', 'Concepts'), ('mappings', 'Mappings')], default='concepts', max_length=10),
        ),
    ]
