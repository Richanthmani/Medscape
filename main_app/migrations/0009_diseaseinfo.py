# Generated by Django 3.2.4 on 2021-06-28 18:36

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_auto_20210604_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='diseaseinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diseasename', models.CharField(max_length=200)),
                ('no_of_symp', models.IntegerField()),
                ('symptomsname', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), size=None)),
                ('confidence', models.DecimalField(decimal_places=2, max_digits=5)),
                ('consultdoctor', models.CharField(max_length=200)),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main_app.patient')),
            ],
        ),
    ]
