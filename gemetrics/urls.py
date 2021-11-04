"""gemetrics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import MetricView, AnalysisView, StepView, \
    save_new_phenotypes, mark_phenotype_as_trained, \
        find_a_non_trained_phenotype_and_mark_as_training, find_trained_phenotype


api = routers.DefaultRouter()
api.register(r"metrics", MetricView)
api.register(r"analysis", AnalysisView)
api.register(r"steps", StepView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(api.urls)),
    path('phenotypes/save_new_phenotypes/', save_new_phenotypes),
    path('phenotypes/mark_as_trained/', mark_phenotype_as_trained),
    path('phenotypes/find_non_trained/', find_a_non_trained_phenotype_and_mark_as_training),
    path('phenotypes/find_trained/', find_trained_phenotype),
]
