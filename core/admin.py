from django.contrib import admin
from core.models import Metric, Analysis

# Register your models here.

class MetricAdmin(admin.ModelAdmin):
    list_filter = ('dataset',)
    list_display = ('dataset', 'phenotype', 'accuracy', 'accuracy_sd', 'f1_score', 'f1_score_sd')
    search_fields = ('phenotype',)
  

class AnalysisAdmin(admin.ModelAdmin):
    list_filter = ('dataset', 'cnn')
    list_display = ('dataset', 'cnn', 'accuracy', 'f1_score', 'size', 'num_layers', 'num_params', 'time')
    search_fields = ('dataset', 'cnn')


admin.site.register(Metric, MetricAdmin)
admin.site.register(Analysis, AnalysisAdmin)