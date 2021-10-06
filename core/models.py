from django.db import models

# Create your models here.

class Metric(models.Model):

    dataset = models.CharField(max_length=20, verbose_name='Dataset name', null=False, blank=False)
    phenotype = models.TextField(verbose_name='Phenotype', null=False)
    accuracy = models.DecimalField(max_digits=22, decimal_places=20, verbose_name='Accuracy')
    accuracy_sd = models.DecimalField(max_digits=22, decimal_places=20, verbose_name='Accuracy SD')
    f1_score = models.DecimalField(max_digits=22, decimal_places=20, verbose_name='F1Score')
    f1_score_sd = models.DecimalField(max_digits=22, decimal_places=20, verbose_name='F1Score SD')

    def __str__(self):
        return self.phenotype

    class Meta:
        verbose_name_plural = 'Metrics'
        ordering = ['-dataset', '-accuracy', '-f1_score']


class Analysis(models.Model):
    
    dataset = models.CharField(max_length=255, verbose_name='Dataset', null=False)
    cnn = models.CharField(max_length=255, verbose_name='CNN', null=False)
    accuracy = models.DecimalField(max_digits=22, decimal_places=20, verbose_name='Accuracy')
    f1_score = models.DecimalField(max_digits=22, decimal_places=20, verbose_name='F1Score')
    size = models.DecimalField(max_digits=22, decimal_places=2, verbose_name='Size')
    num_layers = models.IntegerField(verbose_name='Num. layers')
    num_params = models.IntegerField(verbose_name='Num. params')
    time = models.DecimalField(max_digits=22, decimal_places=6, verbose_name='Time')

    def __str__(self):
        return self.dataset

    class Meta:
        verbose_name_plural = 'Analysis'
        ordering = ['-dataset', '-cnn', '-accuracy', '-f1_score']