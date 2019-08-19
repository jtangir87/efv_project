# Generated by Django 2.1.8 on 2019-08-19 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20190814_0147'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='billingprofile',
            name='address_one',
        ),
        migrations.RemoveField(
            model_name='billingprofile',
            name='address_two',
        ),
        migrations.RemoveField(
            model_name='billingprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='billingprofile',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='billingprofile',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='billingprofile',
            name='state',
        ),
        migrations.RemoveField(
            model_name='billingprofile',
            name='zip_code',
        ),
        migrations.AlterField(
            model_name='billingprofile',
            name='tenant',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='billing', to='customer.Client'),
        ),
    ]
