from core.models import Metric
from rest_framework import serializers


class MetricSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Metric
        fields = ['dataset', 'phenotype', 'accuracy', 'accuracy_sd', 'f1_score', 'f1_score_sd']