from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Blood_donor(models.Model):
    fname = models.TextField(blank=False)
    lname = models.TextField(blank=False)
    email = models.EmailField(unique=True)
    gender = models.TextField(blank=False)
    dob = models.DateField(blank=False)
    nic = models.CharField(max_length=12, blank=False)
    age = models.IntegerField(blank=False)
    weight = models.IntegerField(blank=False)
    city = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

class Blood_recipient(models.Model):
    patient_name = models.TextField(max_length=100)
    gender = models.TextField()
    required_blood_group = models.TextField()
    hospital_name = models.TextField()
    hospital_address = models.TextField()
    city = models.TextField()
    doctor_name = models.TextField()
    when_requried = models.DateTimeField(auto_now=True)
    phone = PhoneNumberField(blank=False, unique=True)
    email = models.EmailField(blank=False)
    reason_for_blood = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

class Event(models.Model):
    event_name = models.TextField(blank=False)
    date = models.DateField(auto_now=True, blank=False)
    time = models.TimeField(auto_now=True, blank=False)
    venue = models.TextField(blank=False)
    img = models.ImageField(upload_to='images', blank=False)
    details = models.TextField(max_length=150, default="")
    description = models.TextField(max_length=1000, default="")

class Message(models.Model):
    full_name = models.TextField(blank=False)
    phone = PhoneNumberField(blank=False, unique=True)
    email = models.EmailField(blank=False, unique=True)
    message = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)


class City(models.Model):
    name = models.TextField()