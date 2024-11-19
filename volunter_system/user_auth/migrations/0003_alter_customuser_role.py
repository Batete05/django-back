# Generated by Django 5.1.2 on 2024-10-25 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_auth', '0002_customuser_role_alter_customuser_groups_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('volunteer', 'Volunteer'), ('organizer', 'Organizer')], default='volunteer', max_length=20),
        ),
    ]