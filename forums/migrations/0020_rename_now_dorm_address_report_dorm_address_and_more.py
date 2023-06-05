# Generated by Django 4.2.1 on 2023-06-05 11:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0019_rename_now_move_how_report_airport_to_campus_mobility_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='report',
            old_name='now_dorm_address',
            new_name='dorm_address',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='now_dorm_cost',
            new_name='dorm_cost',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='now_etc',
            new_name='dorm_etc',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='now_dorm_name',
            new_name='dorm_name',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='now_reputation',
            new_name='dorm_reputation',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='now_website',
            new_name='dorm_website',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='now_is_consult',
            new_name='is_consult',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='now_leisure',
            new_name='leisure',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='now_staff_email',
            new_name='staff_email',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='now_staff_name',
            new_name='staff_name',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='now_staff_position',
            new_name='staff_title',
        ),
        migrations.RenameField(
            model_name='report',
            old_name='now_support',
            new_name='support',
        ),
        migrations.RemoveField(
            model_name='report',
            name='now_semester',
        ),
    ]