# Generated by Django 3.1 on 2020-08-26 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hostelapp', '0002_auto_20200826_2318'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='fees_receipt',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]