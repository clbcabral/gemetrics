# Generated by Django 3.2 on 2021-11-03 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20211028_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='metric',
            name='status',
            field=models.CharField(default='TRAINED', max_length=10, verbose_name='Status'),
        ),
    ]
