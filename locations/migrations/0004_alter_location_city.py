# Generated by Django 3.2.6 on 2021-08-12 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0003_alter_location_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=150, verbose_name='Cidade'),
        ),
    ]