# Generated by Django 4.1.3 on 2023-01-10 05:57

import datetime
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ISPU',
            fields=[
                ('ispu_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
                ('value', models.IntegerField()),
            ],
            options={
                'db_table': 'ispu',
            },
        ),
    ]