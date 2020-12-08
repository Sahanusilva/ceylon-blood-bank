# Generated by Django 3.1.3 on 2020-12-02 10:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blood_recipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_name', models.CharField(max_length=150)),
                ('required_blood_group', models.CharField(max_length=4)),
                ('units', models.CharField(max_length=2)),
                ('hospital_name', models.CharField(max_length=100)),
                ('hospital_address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('doctor_name', models.CharField(max_length=50)),
                ('when_required', models.DateTimeField(blank=True, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('reason_for_blood', models.TextField()),
                ('completed_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(default='Pending', max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=100)),
                ('datetime', models.DateTimeField()),
                ('venue', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='images')),
                ('details', models.CharField(default='', max_length=150)),
                ('description', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=100)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(default='', max_length=100)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blood_donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(default='', max_length=30)),
                ('dob', models.DateField(default='')),
                ('nic', models.CharField(default='', max_length=12)),
                ('city', models.CharField(default='', max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
