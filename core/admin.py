from django.contrib import admin
from core.models import Metric, Analysis, Step

# Register your models here.

class MetricAdmin(admin.ModelAdmin):
    list_filter = ('grammar', 'dataset', 'status')
    list_display = ('grammar', 'dataset', 'phenotype', 'status', 'accuracy', 'accuracy_sd', 'f1_score', 'f1_score_sd', 'time', 'time_sd')
    search_fields = ('phenotype',)
  

class AnalysisAdmin(admin.ModelAdmin):
    list_filter = ('paper', 'dataset', 'cnn')
    list_display = ('paper', 'dataset', 'cnn', 'accuracy', 'f1_score', 'size', 'num_layers', 'num_params', 'time')
    search_fields = ('paper', 'dataset', 'cnn')


class StepAdmin(admin.ModelAdmin):
    list_filter = ('execution', 'grammar', 'dataset', 'generation')
    list_display = ('execution', 'grammar', 'dataset', 'generation', 'phenotype', 'accuracy', 'f1_score', 'time')
    search_fields = ('phenotype',)


admin.site.register(Metric, MetricAdmin)
admin.site.register(Analysis, AnalysisAdmin)
admin.site.register(Step, StepAdmin)