# Generated by Django 4.2.1 on 2023-06-05 11:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0021_rename_airpotr_to_campus_time_report_airport_to_campus_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='course_how',
            new_name='course_procedure',
        ),
    ]