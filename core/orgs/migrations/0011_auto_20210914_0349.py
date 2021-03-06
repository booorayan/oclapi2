# Generated by Django 3.2.7 on 2021-09-14 03:49

from django.db import migrations


def add_org_creator_as_member(apps, schema_editor):
    Organization = apps.get_model('orgs', 'Organization')
    UserProfile = apps.get_model('users', 'UserProfile')
    orgs = Organization.objects.exclude(
        id__in=UserProfile.organizations.through.objects.values_list('organization_id', flat=True)).filter(
        created_by__is_superuser=False
    )
    for org in orgs:
        members = [org.created_by]
        updated_by = org.updated_by
        if not updated_by.is_superuser:
            members.append(updated_by)
        org.members.set(members)


class Migration(migrations.Migration):

    dependencies = [
        ('orgs', '0010_auto_20210720_1000'),
    ]

    operations = [
        migrations.RunPython(add_org_creator_as_member)
    ]
