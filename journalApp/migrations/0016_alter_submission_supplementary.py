# Generated by Django 4.1 on 2023-06-09 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalApp', '0015_alter_submission_manuscript'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='supplementary',
            field=models.FileField(upload_to='papers/%Y/%m/%d/'),
        ),
    ]
