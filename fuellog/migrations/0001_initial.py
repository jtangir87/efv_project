# Generated by Django 2.2.2 on 2019-06-20 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('current', models.CharField(choices=[('EMPTY', 'Empty'), ('1/8', '1/8'), ('1/4', '1/4'), ('1/2', '1/2'), ('3/4', '3/4'), ('FULL', 'Full')], max_length=5)),
                ('after', models.CharField(blank=True, choices=[('EMPTY', 'Empty'), ('1/8', '1/8'), ('1/4', '1/4'), ('1/2', '1/2'), ('3/4', '3/4'), ('FULL', 'Full')], max_length=5)),
                ('gallons', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=5)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=5)),
                ('mileage', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.Vehicle')),
            ],
            options={
                'ordering': ['-date', 'vehicle'],
            },
        ),
    ]
