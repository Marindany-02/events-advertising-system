# Generated by Django 5.1.3 on 2024-11-25 02:24

import django.db.models.deletion
import django.utils.timezone
import event_management_system_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management_system_app', '0003_remove_event_created_at_remove_event_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=event_management_system_app.models.upload_event_image),
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published'), ('Archived', 'Archived')], default='Draft', max_length=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='event',
            name='event_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event_management_system_app.category'),
        ),
    ]