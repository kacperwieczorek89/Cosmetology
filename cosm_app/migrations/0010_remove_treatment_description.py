# Generated by Django 4.0.3 on 2022-03-19 22:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cosm_app', '0009_treatment_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatment',
            name='description',
        ),
    ]