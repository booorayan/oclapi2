# Generated by Django 3.2.8 on 2021-11-02 07:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pins', '0003_auto_20201217_0838'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='created_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='creator_pins', to=settings.AUTH_USER_MODEL),
        ),
    ]
