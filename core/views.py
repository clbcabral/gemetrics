from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
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


@csrf_exempt
def save_new_phenotypes(request):
    if request.method == 'POST':
        grammar = request.POST.get('grammar')
        dataset = request.POST.get('dataset')
        phenotypes = request.POST.getlist('phenotypes')
        # Remove duplicate.
        phenotypes = list(dict.fromkeys(phenotypes))
        bulk = []
        for phenotype in phenotypes:
            if not Metric.objects.filter(grammar=grammar, dataset=dataset, phenotype=phenotype).exists():
                metric = Metric(grammar=grammar, dataset=dataset, phenotype=phenotype)
                metric.accuracy = 0.0
                metric.accuracy_sd = 0.0
                metric.f1_score = 0.0
                metric.f1_score_sd = 0.0
                metric.time = 0.0
                metric.time_sd = 0.0
                metric.status = Metric.NEW
                bulk.append(metric)
        Metric.objects.bulk_create(bulk)
        return JsonResponse({'status': 'ok'})


@csrf_exempt
def mark_phenotype_as_trained(request):
    if request.method == 'POST':
        grammar = request.POST.get('grammar')
        dataset = request.POST.get('dataset')
        phenotype = request.POST.get('phenotype')
        if Metric.objects.filter(grammar=grammar, dataset=dataset, phenotype=phenotype, status=Metric.TRAINING).exists():
            accuracy = request.POST.get('accuracy')
            accuracy_sd = request.POST.get('accuracy_sd')
            f1_score = request.POST.get('f1_score')
            f1_score_sd = request.POST.get('f1_score_sd')
            time = request.POST.get('time')
            time_sd = request.POST.get('time_sd')
            metric = Metric.objects.get(grammar=grammar, dataset=dataset, phenotype=phenotype, status=Metric.TRAINING)
            metric.accuracy = accuracy
            metric.accuracy_sd = accuracy_sd
            metric.f1_score = f1_score
            metric.f1_score_sd = f1_score_sd
            metric.time = time
            metric.time_sd = time_sd
            metric.status = Metric.TRAINED
            metric.save()
        return JsonResponse({'status': 'ok'})


@csrf_exempt
def find_a_non_trained_phenotype_and_mark_as_training(request):
    if request.method == 'POST':
        grammar = request.POST.get('grammar')
        dataset = request.POST.get('dataset')
        metrics = Metric.objects.filter(grammar=grammar, dataset=dataset, status=Metric.NEW).order_by('pk')
        phenotypes = []
        if metrics:
            phenotype = metrics[0].phenotype
            metric = Metric.objects.get(grammar=grammar, dataset=dataset, phenotype=phenotype)
            metric.status = Metric.TRAINING
            metric.save()
            phenotypes.append(phenotype)
        return JsonResponse({'phenotypes': phenotypes})


@csrf_exempt
def find_trained_phenotype(request):
    if request.method == 'POST':
        grammar = request.POST.get('grammar')
        dataset = request.POST.get('dataset')
        phenotype = request.POST.get('phenotype')
        metrics = None
        if Metric.objects.filter(grammar=grammar, dataset=dataset, phenotype=phenotype, status=Metric.TRAINED).exists():
            metric = Metric.objects.get(grammar=grammar, dataset=dataset, phenotype=phenotype, status=Metric.TRAINED)
            metrics = {
                'accuracy': metric.accuracy,
                'accuracy_sd': metric.accuracy_sd,
                'f1_score': metric.f1_score,
                'f1_score_sd': metric.f1_score_sd,
                'time': metric.time,
                'time_sd': metric.time_sd,
            }
        return JsonResponse({'metrics': metrics})