from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from core.models import Metric
from core.serializers import MetricSerializer

# Create your views here.

class MetricView(viewsets.ModelViewSet):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
    filterset_fields = ['dataset', 'phenotype']
    filter_backends = [DjangoFilterBackend]