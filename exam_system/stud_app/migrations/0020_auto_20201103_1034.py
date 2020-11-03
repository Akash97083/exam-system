# Generated by Django 3.1.3 on 2020-11-03 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0019_auto_20201103_1026'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='firstname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='lastname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
