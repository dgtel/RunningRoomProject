# Generated by Django 5.1.5 on 2025-01-24 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_customuser_mobile_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registrationrequest',
            name='lobby_assigned',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='designation',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='mobile_number',
        ),
        migrations.RemoveField(
            model_name='foodtoken',
            name='status_updated_at',
        ),
        migrations.DeleteModel(
            name='CrewCheckInOut',
        ),
        migrations.DeleteModel(
            name='RegistrationRequest',
        ),
    ]
