# Generated by Django 3.1.7 on 2021-03-16 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imageshistorical',
            old_name='id_historical',
            new_name='id_historic',
        ),
    ]