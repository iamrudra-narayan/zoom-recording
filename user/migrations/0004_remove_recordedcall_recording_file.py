# Generated by Django 4.1.7 on 2023-03-01 16:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_alter_recordedcall_date_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recordedcall',
            name='recording_file',
        ),
    ]
