from django.db import models


class Doctor(models.Model):  # E302
    doctor_name = models.CharField(max_length=30)


class Patient(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=30)
    registration_date = models.DateTimeField("date registered")
    waiting_status = models.BooleanField()


class Appointments(models.Model):
    date = models.DateField()
    time = models.TimeField()
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)

    def __main__(self):
        return self
