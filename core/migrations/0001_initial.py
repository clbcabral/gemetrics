# Generated by Django 3.2 on 2021-10-08 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Analysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dataset', models.CharField(max_length=255, verbose_name='Dataset')),
                ('cnn', models.CharField(max_length=255, verbose_name='CNN')),
                ('accuracy', models.DecimalField(decimal_places=20, max_digits=22, verbose_name='Accuracy')),
                ('f1_score', models.DecimalField(decimal_places=20, max_digits=22, verbose_name='F1Score')),
                ('size', models.DecimalField(decimal_places=2, max_digits=22, verbose_name='Size')),
                ('num_layers', models.IntegerField(verbose_name='Num. layers')),
                ('num_params', models.IntegerField(verbose_name='Num. params')),
                ('time', models.DecimalField(decimal_places=6, max_digits=22, verbose_name='Time')),
            ],
            options={
                'verbose_name_plural': 'Analysis',
                'ordering': ['-dataset', '-cnn', '-accuracy', '-f1_score'],
            },
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grammar', models.CharField(max_length=20, verbose_name='Grammar name')),
                ('dataset', models.CharField(max_length=20, verbose_name='Dataset name')),
                ('phenotype', models.TextField(verbose_name='Phenotype')),
                ('accuracy', models.DecimalField(decimal_places=20, max_digits=22, verbose_name='Accuracy')),
                ('accuracy_sd', models.DecimalField(decimal_places=20, max_digits=22, verbose_name='Accuracy SD')),
                ('f1_score', models.DecimalField(decimal_places=20, max_digits=22, verbose_name='F1Score')),
                ('f1_score_sd', models.DecimalField(decimal_places=20, max_digits=22, verbose_name='F1Score SD')),
                ('time', models.DecimalField(decimal_places=6, max_digits=22, verbose_name='Training time')),
                ('time_sd', models.DecimalField(decimal_places=6, max_digits=22, verbose_name='Training time SD')),
            ],
            options={
                'verbose_name_plural': 'Metrics',
                'ordering': ['-grammar', '-dataset', '-accuracy', '-f1_score'],
            },
        ),
    ]
