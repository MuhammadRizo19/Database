from django.contrib import admin
from .models import NeedHelp, Street, City,Country, Contact

admin.site.register(NeedHelp)
admin.site.register(Street)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Contact)