# Generated by Django 4.2.15 on 2025-01-13 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operatingsystems', '0003_os_arch'),
    ]

    operations = [
        migrations.AddField(
            model_name='osgroup',
            name='codename',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
