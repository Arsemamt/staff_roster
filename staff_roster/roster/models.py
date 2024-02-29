from django.db import models

class Shift(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    employee_Id = models.CharField(max_length=10)
    mobile = models.CharField(max_length=20)
    shift = models.ForeignKey(Shift, on_delete=models.CASCADE)