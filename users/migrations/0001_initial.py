# Generated by Django 5.1.7 on 2025-03-17 17:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('specialization', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=10)),
                ('d_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('p_user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PatientDoctorMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('doctor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mappings', to='users.doctor')),
                ('patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mappings', to='users.patient')),
            ],
            options={
                'unique_together': {('patient', 'doctor')},
            },
        ),
    ]
