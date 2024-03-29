# Generated by Django 2.2.4 on 2019-08-28 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Caketang',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200)),
                ('ttl', models.CharField(max_length=20)),
                ('visi', models.CharField(max_length=2000)),
                ('misi', models.CharField(max_length=2000)),
                ('prestasi', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Pemilih',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nim', models.CharField(max_length=8)),
                ('token', models.CharField(max_length=4)),
                ('date', models.DateTimeField(verbose_name='date published')),
                ('vote', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.Caketang')),
            ],
        ),
    ]
