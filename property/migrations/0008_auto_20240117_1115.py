# Generated by Django 3.2.21 on 2024-01-17 08:15

from django.db import migrations
import phonenumbers


def upd_new_owner_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats = Flat.objects.all()
    for flat in flats.iterator():
        phone = phonenumbers.parse(flat.owners_phonenumber, "RU")
        number = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164)
        flat.owner_pure_phone = number
        flat.save()

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_flat_owner_pure_phone'),
    ]

    operations = [migrations.RunPython(upd_new_owner_pure_phone),
    ]