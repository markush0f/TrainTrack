# Generated by Django 5.0.3 on 2024-03-15 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='notice',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='notice_title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
