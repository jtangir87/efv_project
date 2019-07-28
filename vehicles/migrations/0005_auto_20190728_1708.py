# Generated by Django 2.1.8 on 2019-07-28 17:08

from django.db import migrations, models
import vehicles.models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0004_auto_20190718_2152'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='thousand_miles',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='damageimages',
            name='image',
            field=models.ImageField(blank=True, help_text='Take photo horizontally', null=True, upload_to=vehicles.models.update_filename),
        ),
    ]
