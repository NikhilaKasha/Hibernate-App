from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from django.db.models import Sum
import xlwt
from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
import requests
from django.utils.datetime_safe import datetime

import app2
from .models import *
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
import datetime


now = timezone.now()
#def home(request):
#   return render(request, 'app2/home.html',
#                 {'app2': home})

@login_required
def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'app2/customer_list.html',
                 {'customers': customer})

@login_required
def customer_edit(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   if request.method == "POST":
       # update
       form = CustomerForm(request.POST, instance=customer)
       if form.is_valid():
           customer = form.save(commit=False)
           customer.updated_date = timezone.now()
           customer.save()
           customer = Customer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'app2/customer_list.html',
                         {'customers': customer})
   else:
        # edit
       form = CustomerForm(instance=customer)
       return render(request, 'app2/customer_edit.html', {'form': form, 'customers': customer})


# def CustomerForm():
#     pass


@login_required
def customer_new(request):
   if request.method == "POST":
       form = CustomerForm(request.POST)
       if form.is_valid():
           customer = form.save(commit=False)
           customer.created_date = timezone.now()
           customer.save()
           customer = Customer.objects.filter(created_date__lte=timezone.now())
           return redirect( 'app2:customer_list')
   else:
       form = CustomerForm()
       return render(request, 'app2/customer_new.html', {'form': form})

@login_required
def customer_delete(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   customer.delete()
   return redirect('app2:customer_list')

@login_required
def service_list(request):
   services = Service.objects.filter(created_date__lte=timezone.now())
   return render(request, 'app2/service_list.html', {'services': services})

@login_required
def service_new(request):
   if request.method == "POST":
       form = ServiceForm(request.POST)
       if form.is_valid():
           service = form.save(commit=False)
           service.created_date = timezone.now()
           service.save()
           services = Service.objects.filter(created_date__lte=timezone.now())
           return render(request, 'app2/service_list.html',
                         {'services': services})
   else:
       form = ServiceForm()
       # print("Else")
   return render(request, 'app2/service_new.html', {'form': form})

@login_required
def service_edit(request, pk):
   service = get_object_or_404(Service, pk=pk)
   if request.method == "POST":
       form = ServiceForm(request.POST, instance=service)
       if form.is_valid():
           service = form.save()
           # service.customer = service.id
           service.updated_date = timezone.now()
           service.save()
           services = Service.objects.filter(created_date__lte=timezone.now())
           return render(request, 'app2/service_list.html', {'services': services})
   else:
       # print("else")
       form = ServiceForm(instance=service)
   return render(request, 'app2/service_edit.html', {'form': form})

@login_required
def service_delete(request, pk):
   service = get_object_or_404(Service, pk=pk)
   service.delete()
   return redirect('app2:service_list')

@login_required
def summary(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    services = Service.objects.filter(cust_name=pk)
    # product = Product.objects.filter(cust_name=pk)
    sum_service_charge = Service.objects.filter(cust_name=pk).aggregate(Sum('service_charge'))
    # sum_product_charge = Product.objects.filter(cust_name=pk).aggregate(Sum('charge'))
    return render(request, 'app2/summary.html', {'customers': customer,
                                                'services': services,
                                                'sum_service_charge': sum_service_charge})
                                                # 'sum_product_charge': sum_product_charge})
@login_required
def expert_list(request):
    expert = Expert.objects.filter(created_date__lte=timezone.now())
    return render(request, 'app2/expert_list.html', {'experts': expert})

@login_required
def expert_edit(request, pk):
   expert = get_object_or_404(Expert, pk=pk)
   if request.method == "POST":
       # update
       form = ExpertForm(request.POST, instance=expert)
       if form.is_valid():
           expert = form.save(commit=False)
           expert.updated_date = timezone.now()
           expert.save()
           expert = Expert.objects.filter(created_date__lte=timezone.now())
           return render(request, 'app2/expert_list.html',
                         {'experts': expert})
   else:
        # edit
       form =  ExpertForm(instance=expert)
       return render(request, 'app2/expert_edit.html', {'form': form, 'experts': expert})

@login_required
def expert_new(request):
   if request.method == "POST":
       form = ExpertForm(request.POST)
       if form.is_valid():
           expert = form.save(commit=False)
           expert.created_date = timezone.now()
           expert.save()
           expert = Expert.objects.filter(created_date__lte=timezone.now())
           return redirect('app2:expert_list')
   else:
       form = ExpertForm()
       return render(request, 'app2/expert_new.html', {'form': form})

@login_required
def expert_delete(request, pk):
   expert = get_object_or_404(Expert, pk=pk)
   expert.delete()
   return redirect('app2:expert_list')


def contact(request):
    form_class = ContactForm

    return render(request, 'app2/contact.html', {
        'form': form_class,
    })

def about(request):
 return render(request, 'app2/about.html', {'app2': about})