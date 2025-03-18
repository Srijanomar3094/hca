from django.db import models
from django.contrib.auth.models import User

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)
    
    class Meta:
        abstract = True

class Patient(BaseModel):
    p_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='patients')
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Doctor(BaseModel):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    d_user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, related_name='doctor')

    def __str__(self):
        return self.name

class PatientDoctorMapping(BaseModel):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL,null=True, related_name='mappings')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL,null=True, related_name='mappings')

    class Meta:
        unique_together = ('patient', 'doctor')

    def __str__(self):
        return f'{self.patient.name} - {self.doctor.name}'