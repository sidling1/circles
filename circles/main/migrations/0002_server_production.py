# Generated by Django 4.0.6 on 2023-09-08 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='production',
            field=models.BooleanField(default=1),
        ),
    ]
