from django.contrib import admin
from .models import *
# Register your models here.




class CompanyNameAdmin(admin.ModelAdmin):
    list_display = ('company_name',)
    ordering = ('company_name',)

admin.site.register(company_name,CompanyNameAdmin)

class OptionsAdmin(admin.ModelAdmin):
    search_fields=['company_name__company_name']
    ordering = ('company_name__company_name',)

admin.site.register(options, OptionsAdmin)

class ExpiryPriceAdmin(admin.ModelAdmin):
    search_fields=['company_name__company_name']
    ordering = ('company_name__company_name',)

admin.site.register(expirystrikeprice,  ExpiryPriceAdmin)