# Generated by Django 4.1 on 2023-06-08 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journalApp', '0003_journal_abbrv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journal',
            name='pic',
            field=models.ImageField(blank=True, default='static/assets/imgs/vaccines-11-00991-g001-550.jpg', null=True, upload_to=''),
        ),
    ]
