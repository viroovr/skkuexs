# Generated by Django 4.2.1 on 2023-06-01 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forums', '0006_alter_article_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='introduction',
            field=models.TextField(blank=True, null=True),
        ),
    ]
