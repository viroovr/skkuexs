# Generated by Django 4.2.1 on 2023-06-05 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0016_rename_user_duration_report_semester_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='visa_how',
            new_name='visa_issuance_procedure',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='visa_issue_time',
            new_name='visa_issuance_time',
        ),
    ]
