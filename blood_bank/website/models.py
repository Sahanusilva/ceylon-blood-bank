from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
from phonenumber_field.modelfields import PhoneNumberField


class Blood_donor(models.Model):    
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    gender = models.CharField(max_length=30 , blank=False, default='')
    dob = models.DateField(blank=False, default='')
    nic = models.CharField(max_length=12, blank=False, default='')
    city = models.CharField(max_length=30 , default='')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    # post_save.connect(create_profile, sender=User)

class Blood_recipient(models.Model):
    patient_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=6) 
    required_blood_group = models.CharField(max_length=4)
    units = models.CharField(max_length=2)
    hospital_name = models.CharField(max_length=100)
    hospital_address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    doctor_name = models.CharField(max_length=50)
    when_required = models.DateTimeField(null=True, blank=True)
    phone = PhoneNumberField(blank=False, unique=False)
    email = models.EmailField(blank=False)
    reason_for_blood = models.TextField()
    completed_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=50, null=False, blank=False, default='Pending')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name

class Event(models.Model):
    event_name = models.CharField(max_length=100 ,blank=False)
    datetime = models.DateTimeField(blank=False)
    venue = models.CharField(max_length=200 ,blank=False)
    img = models.ImageField(upload_to='images', blank=False)
    details = models.CharField(max_length=150, default="")
    description = models.TextField(default="")
    
    def __str__(self):
        return self.event_name


class Message(models.Model):
    fullname = models.CharField(max_length=100, blank=False)
    phone = PhoneNumberField(blank=False, unique=False)
    email = models.EmailField(blank=False, unique=False)
    subject = models.CharField(max_length=100,blank=False, default='')
    message = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


class City(models.Model):
    name = models.TextField()