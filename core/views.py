from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Metric, Analysis, Step
from core.serializers import MetricSerializer, AnalysisSerializer, StepSerializer

# Create your views here.

class MetricView(viewsets.ModelViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    filterset_fields = ['grammar', 'dataset', 'phenotype']
    filter_backends = [DjangoFilterBackend]


class AnalysisView(viewsets.ModelViewSet):
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer
    filterset_fields = ['dataset', 'cnn']
    filter_backends = [DjangoFilterBackend]


class StepView(viewsets.ModelViewSet):
    queryset = Step.objects.all()
    serializer_class = StepSerializer
    filterset_fields = ['execution']
    filter_backends = [DjangoFilterBackend]