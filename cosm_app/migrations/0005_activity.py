# Generated by Django 4.0.3 on 2022-03-17 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cosm_app', '0004_remove_producttype_product_types_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('time', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
            ],
        ),
    ]
