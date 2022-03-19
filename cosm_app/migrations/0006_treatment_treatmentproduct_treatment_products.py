# Generated by Django 4.0.3 on 2022-03-18 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cosm_app', '0005_activity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cosm_app.product')),
                ('treatment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cosm_app.treatment')),
            ],
        ),
        migrations.AddField(
            model_name='treatment',
            name='products',
            field=models.ManyToManyField(through='cosm_app.TreatmentProduct', to='cosm_app.product'),
        ),
    ]
