# Generated by Django 4.1 on 2023-06-10 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('journalApp', '0017_submission_journal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='journal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='journalApp.journal'),
        ),
    ]
