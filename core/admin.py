from django.contrib import admin
from core.models import Metric

# Register your models here.

class MetricAdmin(admin.ModelAdmin):
    list_display = ('dataset', 'phenotype', 'accuracy', 'accuracy_sd', 'f1_score', 'f1_score_sd')
  

admin.site.register(Metric, MetricAdmin)