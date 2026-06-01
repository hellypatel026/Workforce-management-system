from django.db import models
from departments.models import Department
from django.conf import settings


class Employee(models.Model):

    ROLE_CHOICES = (
        ('hr', 'HR'),
        ('manager', 'Manager'),
        ('worker', 'Worker'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    employee_id = models.CharField(max_length=20, unique=True)

    role = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES
    )

    full_name = models.CharField(max_length=100)

    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )

    designation = models.CharField(max_length=100)

    joining_date = models.DateField()

    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.employee_id} - {self.full_name}"