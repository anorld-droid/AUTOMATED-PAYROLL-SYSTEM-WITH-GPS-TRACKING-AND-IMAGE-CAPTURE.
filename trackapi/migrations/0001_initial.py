# Generated by Django 3.2.3 on 2022-04-26 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import trackapi.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('one_hour', models.CharField(blank=True, max_length=100, null=True)),
                ('two_hours', models.CharField(blank=True, max_length=100, null=True)),
                ('three_hours', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basic_salary', models.IntegerField()),
                ('commission', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('image', models.ImageField(upload_to=trackapi.models.employee_directory_path)),
                ('job_name', models.CharField(max_length=50)),
                ('hire_date', models.DateField()),
                ('status', models.CharField(max_length=4)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackapi.department')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackapi.location')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to=settings.AUTH_USER_MODEL)),
                ('salary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trackapi.salary')),
            ],
            options={
                'ordering': ['hire_date'],
            },
        ),
    ]
