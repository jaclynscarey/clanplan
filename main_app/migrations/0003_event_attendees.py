# Generated by Django 4.2.1 on 2023-06-10 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_attendee_rsvp_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='attendees',
            field=models.ManyToManyField(to='main_app.userprofile'),
        ),
    ]
