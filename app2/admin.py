

# Register your models here.
from django.contrib import admin

from .models import Customer, Service, Expert


class CustomerList(admin.ModelAdmin):
    list_display = ('cust_name', 'cust_number', 'email', 'phone_number')
    list_filter = ('cust_name', 'cust_number')
    search_fields = ('cust_name', 'cust_number')
    ordering = ['cust_name']


class ServiceList(admin.ModelAdmin):
    list_display = ('cust_name', 'service_category', 'location', 'appointment')
    list_filter = ('cust_name', 'service_category', 'location')
    search_fields = ('cust_name', 'location')
    ordering = ['cust_name', 'service_category']

class ExpertList(admin.ModelAdmin):
    list_display = ('expert_name', 'email', 'phone_number')
    list_filter = ('expert_name', 'phone_number')
    search_fields = ('expert_name', 'phone_number')
    ordering = ['expert_name']


admin.site.register(Customer, CustomerList)
admin.site.register(Service, ServiceList)
admin.site.register(Expert, ExpertList)
