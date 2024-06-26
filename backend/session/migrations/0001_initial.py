# Generated by Django 5.0.3 on 2024-03-14 23:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0006_remove_parent_token_jwt_remove_trainer_token_jwt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_title', models.CharField(blank=True, max_length=300, null=True)),
                ('session_description', models.CharField(blank=True, max_length=300, null=True)),
                ('session_created_at', models.CharField(blank=True, max_length=300, null=True)),
                ('notification_title', models.CharField(blank=True, max_length=300, null=True)),
                ('notification', models.CharField(blank=True, max_length=300, null=True)),
                ('notification_created_at', models.CharField(blank=True, max_length=300, null=True)),
                ('player', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='get_players_session', to='members.player', verbose_name='Players')),
                ('trainer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='get_trainers_session', to='members.trainer', verbose_name='Trainer')),
            ],
        ),
    ]
