from account.models import CustomizedUser
from django.db import models


class Appointment(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    doctor = models.ForeignKey(
        CustomizedUser, on_delete=models.CASCADE, related_name="doctor"
    )
    patient = models.ForeignKey(
        CustomizedUser,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="patient",
    )
    meeting_link = models.URLField(blank=True)
    status_option = {
        ("active", "active"),
        ("cancelled", "cancelled"),
    }
    status = models.CharField(max_length=10, choices=status_option, default="active")
