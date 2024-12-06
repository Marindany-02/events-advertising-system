# Generated by Django 5.1.3 on 2024-11-26 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management_system_app', '0006_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.CharField(choices=[('Technology', 'Technology'), ('Education', 'Education'), ('Culture', 'Culture'), ('Sports', 'Sports'), ('Religious', 'Religious'), ('Other', 'Other')], max_length=50),
        ),
    ]
