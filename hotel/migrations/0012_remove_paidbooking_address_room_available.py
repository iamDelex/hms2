# Generated by Django 4.0.4 on 2022-05-27 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0011_alter_paidbooking_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paidbooking',
            name='address',
        ),
        migrations.AddField(
            model_name='room',
            name='available',
            field=models.BooleanField(default=True),
        ),
    ]
