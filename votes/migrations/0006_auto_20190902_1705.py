# Generated by Django 2.2.4 on 2019-09-02 10:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0005_token_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pemilih',
            name='token',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='votes.Token'),
        ),
        migrations.AlterField(
            model_name='pemilih',
            name='vote',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='votes.Caketang'),
        ),
    ]
