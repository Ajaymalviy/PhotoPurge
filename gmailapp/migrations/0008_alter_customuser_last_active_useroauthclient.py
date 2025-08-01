# Generated by Django 5.1.4 on 2025-03-27 20:34

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gmailapp', '0007_alter_customuser_last_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='last_active',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 3, 27, 20, 34, 12, 634239, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.CreateModel(
            name='UserOAuthClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=255, unique=True)),
                ('client_secret', models.CharField(max_length=255, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
