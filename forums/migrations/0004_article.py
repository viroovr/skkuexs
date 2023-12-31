# Generated by Django 4.2.1 on 2023-05-31 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0003_delete_school_report_rank'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_university', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('context', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('recommand', models.IntegerField()),
                ('comment', models.IntegerField()),
            ],
        ),
    ]
