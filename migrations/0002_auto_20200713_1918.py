# Generated by Django 2.2.10 on 2020-07-13 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='title',
            field=models.CharField(default='', max_length=1000, verbose_name='название опроса'),
        ),
    ]
