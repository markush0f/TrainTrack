# Generated by Django 5.0.2 on 2024-04-13 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0010_remove_calendar_dateevent_calendar_event_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='calendar',
            name='event_date',
            field=models.CharField(default=11, max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calendar',
            name='event_time',
            field=models.DateField(),
        ),
    ]
