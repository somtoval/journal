# Generated by Django 4.1 on 2023-06-07 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HomeSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('body', models.TextField(null=True)),
                ('pic', models.ImageField(blank=True, default='assets/imgs/vaccines-11-00991-g001-550.jpg', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('about', models.CharField(blank=True, max_length=200, null=True)),
                ('impact', models.FloatField(blank=True, null=True)),
                ('pic', models.ImageField(blank=True, default='assets/imgs/vaccines-11-00991-g001-550.jpg', null=True, upload_to='')),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('category', models.ManyToManyField(to='journalApp.category')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('body', models.TextField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.FloatField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('journal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='journalApp.journal')),
            ],
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('author', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('doi', models.CharField(max_length=200, null=True)),
                ('issue', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='journalApp.issue')),
                ('journal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='journalApp.journal')),
            ],
        ),
        migrations.AddField(
            model_name='issue',
            name='journal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='journalApp.journal'),
        ),
        migrations.AddField(
            model_name='issue',
            name='volume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='journalApp.volume'),
        ),
    ]
