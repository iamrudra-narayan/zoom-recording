# Generated by Django 4.1.7 on 2023-03-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordedcall',
            name='recording_file',
            field=models.CharField(max_length=50000),
        ),
    ]
