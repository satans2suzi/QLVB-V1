from django.contrib import admin

# Register your models here.
from .models import DomainName, Offenses


class DomainNameAdmin(admin.ModelAdmin):
    list_display = ('domainID', 'domainName')


class OffensesAdmin(admin.ModelAdmin):
    list_display = ('number', 'timestamp', 'offensenID', 'domainID',
                    'descriptions', 'category', 'sourceIP', 'destinationIP', 'severity')


admin.site.register(DomainName, DomainNameAdmin)
admin.site.register(Offenses, OffensesAdmin)
