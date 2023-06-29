from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import NeedHelp, Street, City, Contact
from django.db.models import Q, F
from django.core.paginator import Paginator, EmptyPage
from .forms import ContactForm
from django.urls import reverse_lazy

class HomePage(LoginRequiredMixin, generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['streets'] = Street.objects.all().count()
        context['needs'] = NeedHelp.objects.all().count()
        return context

class ContactList(generic.ListView):
    template_name = 'orm.html'
    model = Contact
    context_object_name = 'contacts'
    paginate_by = 3

class AddContact(generic.CreateView):
    template_name = 'new.html'
    model = Contact
    success_url = reverse_lazy('contacts')
    form_class = ContactForm

class ChangeContact(generic.UpdateView):
     template_name = 'change.html'
     form_class = ContactForm
     model = Contact
     success_url = reverse_lazy('contacts')
     context_object_name = 'contact'

class ContactDetail(generic.DetailView):
     template_name = 'detail.html'
     model = Contact
     context_object_name = 'contact'

def delete_contact(request, contact_id):
	contact = Contact.objects.get(id=contact_id)
	contact.delete()
	return redirect('contacts')

def search(request):
     if request.method == 'POST':
          search = request.POST['qidir']
          contact = Contact.objects.filter(firstName__contains=search)
          street = Street.objects.filter(streetName__contains=search)
          return render(request, 'search.html', {'searched':search, 'contact':contact, 'street':street})
          

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