# Generated by Django 3.2.3 on 2022-04-25 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trackapi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='employee',
            name='f_name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='employee',
            name='job_name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='l_name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='location',
            name='one_hour',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='three_hours',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='location',
            name='two_hours',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
