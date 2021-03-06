# Generated by Django 3.2 on 2022-02-02 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_metric_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analysis',
            options={'ordering': ['paper', '-dataset', '-cnn', '-accuracy', '-f1_score'], 'verbose_name_plural': 'Analysis'},
        ),
        migrations.AddField(
            model_name='analysis',
            name='paper',
            field=models.CharField(max_length=255, null=True, verbose_name='Paper'),
        ),
    ]
