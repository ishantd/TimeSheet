# Generated by Django 3.0.3 on 2020-05-06 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200506_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='report_extended',
            name='extended_hours',
            field=models.BooleanField(default=False),
        ),
    ]
