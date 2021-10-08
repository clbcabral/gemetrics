from core.models import Metric, Analysis
from rest_framework import serializers


class MetricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Metric
        fields = ['grammar', 'dataset', 'phenotype', 'accuracy', 'accuracy_sd', 'f1_score', 'f1_score_sd', 'time', 'time_sd']


class AnalysisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Analysis
        fields = ['dataset', 'cnn', 'accuracy', 'f1_score', 'size', 'num_layers', 'num_params', 'time']