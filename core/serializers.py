from core.models import Metric, Analysis, Step
from rest_framework import serializers


class MetricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Metric
        fields = ['grammar', 'dataset', 'phenotype', 'status', 'accuracy', 'accuracy_sd', 'f1_score', 'f1_score_sd', 'time', 'time_sd']


class AnalysisSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Analysis
        fields = ['paper', 'dataset', 'cnn', 'accuracy', 'f1_score', 'size', 'num_layers', 'num_params', 'time']


class StepSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Step
        fields = ['execution', 'grammar', 'dataset', 'generation', 'phenotype', 'accuracy', 'f1_score', 'time']