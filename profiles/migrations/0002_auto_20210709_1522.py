# Generated by Django 3.2.5 on 2021-07-09 15:22

from django.apps import apps as global_apps
from django.db import migrations


def migrate_profiles(apps, schema_editor):
    try:
        OldModel = apps.get_model('oc_lettings_site', 'Profile')
    except LookupError:
        return   
    NewProfile = apps.get_model('profiles', 'Profile')
    NewProfile.objects.bulk_create(
        NewProfile( user=old_object.user, favorite_city=old_object.favorite_city)
        for old_object in OldModel.objects.all()
    )


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_profiles)
    ]

    #if global_apps.is_installed('oc_lettings_site'):
    #    dependencies.append(('oc_lettings_site', '0001_initial'))
