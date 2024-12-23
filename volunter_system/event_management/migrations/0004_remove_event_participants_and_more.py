# Generated by Django 5.1.2 on 2024-11-22 08:50

import django.db.models.deletion
import event_management.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0003_alter_eventparticipation_unique_together_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='participants',
        ),
        migrations.AlterField(
            model_name='eventparticipation',
            name='participant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participations', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='eventparticipation',
            name='user',
            field=models.ForeignKey(default=event_management.models.get_default_user, on_delete=django.db.models.deletion.CASCADE, related_name='event_participations', to=settings.AUTH_USER_MODEL),
        ),
    ]
