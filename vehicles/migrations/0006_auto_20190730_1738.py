# Generated by Django 2.1.8 on 2019-07-30 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0005_auto_20190728_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehicle',
            old_name='thousand_miles',
            new_name='five_hundred_miles',
        ),
    ]
