from typing import Any, Dict
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import NeedHelp, Street

class HomePage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['streets'] = Street.objects.all().count()
        context['needs'] = NeedHelp.objects.all().count()
        return context