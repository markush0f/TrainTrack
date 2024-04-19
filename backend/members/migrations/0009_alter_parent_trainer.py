# Generated by Django 5.0.2 on 2024-03-29 20:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0008_alter_parent_trainer_alter_trainer_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parent',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_trainers', to='members.trainer', verbose_name='Trainer'),
        ),
    ]