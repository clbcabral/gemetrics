from django.db import models

# Create your models here.

class Metric(models.Model):

    dataset = models.CharField(max_length=20, verbose_name='Dataset name', null=False, blank=False)
    phenotype = models.CharField(max_length=255, verbose_name='Phenotype', null=False)
    accuracy = models.DecimalField(max_digits=22, decimal_places=20, verbose_name='Accuracy')
    accuracy_sd = models.DecimalField(max_digits=22, decimal_places=20, verbose_name='Accuracy SD')
    f1_score = models.DecimalField(max_digits=22, decimal_places=20, verbose_name='F1Score')
    f1_score_sd = models.DecimalField(max_digits=22, decimal_places=20, verbose_name='F1Score SD')

    def __str__(self):
        return self.phenotype

    class Meta:
        verbose_name_plural = 'Metrics'
        ordering = ['-dataset', '-accuracy', '-f1_score']