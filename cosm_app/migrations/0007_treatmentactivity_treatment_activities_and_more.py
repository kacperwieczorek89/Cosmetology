# Generated by Django 4.0.3 on 2022-03-18 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cosm_app', '0006_treatment_treatmentproduct_treatment_products'),
    ]

    operations = [
        migrations.CreateModel(
            name='TreatmentActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cosm_app.activity')),
            ],
        ),
        migrations.AddField(
            model_name='treatment',
            name='activities',
            field=models.ManyToManyField(through='cosm_app.TreatmentActivity', to='cosm_app.activity'),
        ),
        migrations.AddField(
            model_name='treatmentactivity',
            name='treatment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cosm_app.treatment'),
        ),
    ]