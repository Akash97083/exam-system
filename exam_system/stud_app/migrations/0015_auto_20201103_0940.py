# Generated by Django 3.1.3 on 2020-11-03 04:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stud_app', '0014_auto_20201102_2358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course_fk',
            field=models.ManyToManyField(blank=True, null=True, to='stud_app.Course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='dept_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stud_app.department'),
        ),
    ]
