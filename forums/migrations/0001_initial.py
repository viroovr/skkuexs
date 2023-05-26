# Generated by Django 4.2.1 on 2023-05-25 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_department', models.CharField(blank=True, max_length=200, null=True)),
                ('user_type', models.CharField(blank=True, max_length=200, null=True)),
                ('user_country', models.CharField(blank=True, max_length=200, null=True)),
                ('user_university', models.CharField(blank=True, max_length=200, null=True)),
                ('user_duration', models.CharField(blank=True, max_length=200, null=True)),
                ('pre_visa_type', models.CharField(blank=True, max_length=200, null=True)),
                ('pre_visa_apply_duration', models.CharField(blank=True, max_length=200, null=True)),
                ('pre_visa_how', models.CharField(blank=True, max_length=200, null=True)),
                ('pre_visa_ready_check', models.CharField(blank=True, max_length=200, null=True)),
                ('pre_dorm_register', models.CharField(blank=True, max_length=200, null=True)),
                ('pre_class_register', models.CharField(blank=True, max_length=200, null=True)),
                ('pre_etc', models.CharField(blank=True, max_length=200, null=True)),
                ('now_move_how', models.CharField(blank=True, max_length=200, null=True)),
                ('now_move_time', models.CharField(blank=True, max_length=200, null=True)),
                ('now_semester', models.CharField(blank=True, max_length=200, null=True)),
                ('now_dorm_name', models.CharField(blank=True, max_length=200, null=True)),
                ('now_cost', models.CharField(blank=True, max_length=200, null=True)),
                ('now_dorm_address', models.CharField(blank=True, max_length=200, null=True)),
                ('now_reputation', models.CharField(blank=True, max_length=200, null=True)),
                ('now_website', models.CharField(blank=True, max_length=200, null=True)),
                ('now_etc', models.CharField(blank=True, max_length=200, null=True)),
                ('now_leisure', models.CharField(blank=True, max_length=200, null=True)),
                ('now_staff_name', models.CharField(blank=True, max_length=200, null=True)),
                ('now_staff_position', models.CharField(blank=True, max_length=200, null=True)),
                ('now_staff_email', models.CharField(blank=True, max_length=200, null=True)),
                ('now_is_consult', models.CharField(blank=True, max_length=200, null=True)),
                ('now_support', models.CharField(blank=True, max_length=200, null=True)),
                ('course_num', models.CharField(blank=True, max_length=200, null=True)),
                ('course_name', models.CharField(blank=True, max_length=200, null=True)),
                ('course_reputation', models.CharField(blank=True, max_length=200, null=True)),
                ('course_how', models.CharField(blank=True, max_length=200, null=True)),
                ('course_grading', models.CharField(blank=True, max_length=200, null=True)),
                ('course_website', models.CharField(blank=True, max_length=200, null=True)),
                ('course_etc', models.CharField(blank=True, max_length=200, null=True)),
                ('post_flight', models.CharField(blank=True, max_length=200, null=True)),
                ('post_ready_check', models.CharField(blank=True, max_length=200, null=True)),
                ('post_dorm_end', models.CharField(blank=True, max_length=200, null=True)),
                ('post_how_end', models.CharField(blank=True, max_length=200, null=True)),
                ('post_etc', models.CharField(blank=True, max_length=200, null=True)),
                ('etc_good', models.CharField(blank=True, max_length=200, null=True)),
                ('etc_feel', models.CharField(blank=True, max_length=200, null=True)),
                ('ect_say', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(blank=True, max_length=50, null=True)),
                ('period', models.CharField(blank=True, max_length=50, null=True)),
                ('website', models.CharField(blank=True, max_length=100, null=True)),
                ('impression', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
