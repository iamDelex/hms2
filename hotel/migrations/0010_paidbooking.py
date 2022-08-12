# Generated by Django 4.0.4 on 2022-05-04 15:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hotel', '0009_alter_booking_no_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaidBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('cart_no', models.CharField(blank=True, max_length=36, null=True)),
                ('payment_code', models.CharField(max_length=36)),
                ('paid_item', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'PaidBooking',
                'verbose_name_plural': 'PaidBooking',
                'db_table': 'paidBooking',
                'managed': True,
            },
        ),
    ]