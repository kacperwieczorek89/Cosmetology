# Generated by Django 4.0.1 on 2022-01-29 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosm_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producttypes',
            name='product_type_plural',
            field=models.CharField(default='N/A', max_length=15),
        ),
    ]
