# Generated by Django 5.1.3 on 2024-11-25 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management_system_app', '0004_event_image_event_status_alter_event_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image',
        ),
        migrations.RemoveField(
            model_name='event',
            name='status',
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
