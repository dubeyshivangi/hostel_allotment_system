# Generated by Django 3.1 on 2020-08-26 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='vacant',
        ),
        migrations.RemoveField(
            model_name='student',
            name='fee_receipt',
        ),
        migrations.AlterField(
            model_name='student',
            name='student_contact',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
