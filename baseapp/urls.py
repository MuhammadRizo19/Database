from django.urls import path
from .views import HomePage, stats_chart, ContactList, AddContact, delete_contact, ChangeContact, ContactDetail


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('stats', stats_chart, name='stats'),
    path('delete_contact/<contact_id>', delete_contact, name='delete_contact'),
    path('add', AddContact.as_view(), name='addnew'),
    path('contacts/<uuid:pk>/edit/', ChangeContact.as_view(), name='contact_edit'),
    path('contacts/<uuid:pk>/detail/', ContactDetail.as_view(), name='contact_detail'),
    path('contacts', ContactList.as_view(), name='contacts'),
]