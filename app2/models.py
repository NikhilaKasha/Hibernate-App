from django.db import models
from django.utils import timezone


# Create your models here.
Gender = (
        ('--', "--"),
        ('Male', "Male"),
        ('Female', "Female"),
)
class Expert(models.Model):
    expert_name = models.CharField(max_length=50, verbose_name='Expert Name')
    expert_category = models.CharField(max_length=20, choices=(( 'salon expert', 'salon expert'), ('Appliance expert', 'Appliance expert'), ( 'Cleaning expert', 'Cleaning expert'),( 'Fitness expert','Fitness expert'),( 'General expert','General expert')))
    email = models.EmailField(max_length=100)
    Gender = models.CharField(max_length=15, choices=Gender, default='--', verbose_name="Gender")
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(


    default = timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)


    def created(self):
      self.created_date = timezone.now()
      self.save()


    def updated(self):
      self.updated_date = timezone.now()
      self.save()


    def __str__(self):
      return str(self.expert_name)

class Customer(models.Model):
    cust_name = models.CharField(max_length=50, verbose_name='Name')
    cust_number = models.IntegerField(blank=False, null=False)
    email = models.EmailField(max_length=100)
    Gender = models.CharField(max_length = 15, choices = Gender, default = '--', verbose_name= "Gender")
    address = models.CharField(max_length=200)
    account_number = models.IntegerField(blank=False, null=False)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=50)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_name)

class Service(models.Model):
    cust_name = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='services')
    service_category = models.CharField(max_length=20, choices=(( 'salon service', 'salon service'), ('Appliance service', 'Appliance service'), ( 'Cleaning service', 'Cleaning service'),( 'Fitness service','Fitness service'),( 'General service','General service')))
    description = models.TextField(max_length=500,blank=False, null=False)
    location = models.CharField(max_length=20, choices=(( 'Salt lake city', 'Salt lake city'), ( 'Omaha', 'Omaha'), ( 'Chicago','Chicago'),( 'Denver', 'Denver')))
    appointment_date_time = models.DateTimeField(
        default=timezone.now)
    service_charge = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(
        default=timezone.now)
    updated_date = models.DateTimeField(auto_now_add=True)

    def appointment(self):
        self.appointment_date = timezone.now()
        self.save()

    def created(self):
        self.created_date = timezone.now()
        self.save()

    def updated(self):
        self.updated_date = timezone.now()
        self.save()

    def __str__(self):
        return str(self.cust_name)