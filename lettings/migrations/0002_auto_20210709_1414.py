# Generated by Django 3.2.5 on 2021-07-09 14:14
from django.apps import apps as global_apps
from django.db import migrations


def migrate_address(apps, schema_editor):
    try:
        OldModel = apps.get_model('oc_lettings_site', 'Address')
    except LookupError:
        return   
    NewAddress = apps.get_model('lettings', 'Address')
    NewAddress.objects.bulk_create(
        NewAddress(
            number=old_object.number,
            street=old_object.street,
            city=old_object.city,
            state=old_object.state,
            zip_code=old_object.zip_code,
            country_iso_code=old_object.country_iso_code
        )
        for old_object in OldModel.objects.all()
    )

def migrate_lettings(apps, schema_editor):
    try:
        OldModel = apps.get_model('oc_lettings_site', 'Letting')
    except LookupError:
        return   
    NewLetting = apps.get_model('lettings', 'Letting')
    NewLetting.objects.bulk_create(
        NewLetting(
            title=old_object.title,
            address_id= old_object.address_id
        ) 
        for old_object in OldModel.objects.all()
    )


class Migration(migrations.Migration):

    dependencies = [
        ('lettings', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(migrate_address),
        migrations.RunPython(migrate_lettings),
    ]

    #if global_apps.is_installed('oc_lettings_site'):
    #    dependencies.append(('oc_lettings_site', '0001_initial'))
