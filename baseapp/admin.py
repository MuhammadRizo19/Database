from django.contrib import admin
from .models import NeedHelp, Street, City,Country

admin.site.register(NeedHelp)
admin.site.register(Street)
admin.site.register(Country)
admin.site.register(City)