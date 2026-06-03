from employees.models import Employee
from django.db import models

class Attendance(models.Model):

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE
    )

    date = models.DateField()

    check_in = models.TimeField(
        null=True,
        blank=True
    )

    check_out = models.TimeField(
        null=True,
        blank=True
    )

    status = models.CharField(
        max_length=10,
        choices=[
            ('Present', 'Present'),
            ('Absent', 'Absent'),
        ],
        default='Present'
    )

    def __str__(self):
        return f"{self.employee.full_name} - {self.date}"