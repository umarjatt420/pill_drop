# Generated by Django 4.1.2 on 2024-06-10 07:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0002_alter_medicine_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='medicine',
            old_name='image_url',
            new_name='image',
        ),
    ]
