from django import forms
from .models import Customer, Service, Expert

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('cust_name','Gender', 'email','cust_number','account_number', 'city', 'zipcode')

class ServiceForm(forms.ModelForm):
   class Meta:
       model = Service
       fields = ('cust_name', 'service_category', 'description', 'location', 'appointment_date_time', 'service_charge')

class ExpertForm(forms.ModelForm):
    class Meta:
        model = Expert
        fields = ('expert_name','Gender', 'email','address', 'city','state', 'zipcode')


class ContactForm(forms.Form):
    Name = forms.CharField(required=True)
    Email = forms.EmailField(required=True)
    Subject=forms.CharField(required=False)
    Message = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
