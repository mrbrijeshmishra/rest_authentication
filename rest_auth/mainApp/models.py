from django.db import models

class Company(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class Employee(models.Model):
    eid = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    salary = models.IntegerField()
    email = models.EmailField(max_length=150)

