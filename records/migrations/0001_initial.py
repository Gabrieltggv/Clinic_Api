# Generated by Django 3.1.6 on 2021-02-09 02:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scheduling', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Records',
            fields=[
                ('id_historic', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('appearance_symptoms', models.CharField(blank=True, max_length=100, null=True)),
                ('duration_symptoms', models.CharField(blank=True, max_length=100, null=True)),
                ('local_pain', models.CharField(blank=True, max_length=100, null=True)),
                ('kind_pain', models.CharField(blank=True, max_length=100, null=True)),
                ('conclusion', models.CharField(blank=True, max_length=100, null=True)),
                ('id_scheduling', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='records', to='scheduling.appointments')),
            ],
            options={
                'db_table': 'records',
                'managed': True,
            },
        ),
    ]