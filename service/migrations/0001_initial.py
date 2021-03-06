# Generated by Django 2.2.2 on 2019-06-20 00:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, default=django.utils.timezone.now, null=True)),
                ('servicer', models.CharField(blank=True, max_length=100)),
                ('invoice', models.CharField(blank=True, max_length=100)),
                ('cost', models.DecimalField(blank=True, decimal_places=2, default='0', max_digits=7)),
                ('mileage', models.IntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True)),
                ('completed', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicles.Vehicle')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
