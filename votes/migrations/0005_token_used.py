# Generated by Django 2.2.4 on 2019-08-30 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0004_auto_20190830_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='used',
            field=models.BooleanField(default=False),
        ),
    ]
