# Generated by Django 4.0.3 on 2022-03-19 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosm_app', '0007_treatmentactivity_treatment_activities_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
