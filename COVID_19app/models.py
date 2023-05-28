from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField()

class Patient(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    date_of_birth = models.DateField()

class Report(models.Model):
    STATUS_CHOICES = (
        ('Negative', 'Negative'),
        ('Travelled-Quarantine', 'Travelled-Quarantine'),
        ('Symptoms-Quarantine', 'Symptoms-Quarantine'),
        ('Positive-Admit', 'Positive-Admit'),
    )

    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_date = models.DateTimeField(auto_now_add=True)
