# Generated by Django 4.1 on 2023-06-09 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalApp', '0008_paper_recieved'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200, null=True)),
                ('lastname', models.CharField(max_length=200, null=True)),
                ('email', models.EmailField(max_length=200, null=True)),
                ('phonenumber', models.CharField(max_length=200, null=True)),
                ('institution', models.CharField(max_length=200, null=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('manuscript', models.FileField(upload_to='uploads/% Y/% m/% d/')),
                ('supplementary', models.FileField(upload_to='uploads/% Y/% m/% d/')),
            ],
        ),
    ]
