# Generated by Django 5.1.2 on 2024-10-25 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
