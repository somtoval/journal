# Generated by Django 4.1 on 2023-06-08 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalApp', '0002_remove_journal_category_delete_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='journal',
            name='abbrv',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]