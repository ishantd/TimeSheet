# Generated by Django 3.0.3 on 2020-05-10 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_project_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='overrun',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_type',
            field=models.CharField(choices=[('Overhead', 'Overhead'), ('BD', 'BD'), ('Chargeable', 'Chargeable'), ('Development', 'Development')], max_length=200, null=True),
        ),
    ]