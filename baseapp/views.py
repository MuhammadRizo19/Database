from typing import Any, Dict
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import NeedHelp, Street, City

class HomePage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['streets'] = Street.objects.all().count()
        context['needs'] = NeedHelp.objects.all().count()
        return context

def stats_chart(request):
    labels = []
    data = []

    queryset = City.objects.order_by('-population')[:5]
    for city in queryset:
        labels.append(city.name)
        data.append(city.population)

    return render(request, 'stats.html', {
        'labels': labels,
        'data': data,
    })