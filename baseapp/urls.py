from django.urls import path
from .views import HomePage, stats_chart

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('stats', stats_chart, name='stats')
]