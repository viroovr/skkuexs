# Generated by Django 4.2.1 on 2023-06-05 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0020_rename_now_dorm_address_report_dorm_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='airpotr_to_campus_time',
            new_name='airport_to_campus_time',
        ),
    ]
