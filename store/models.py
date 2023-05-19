from django.db import models
from django.db import connections

# Create your models here.
class Medicinedetails(models.Model):
    medicine_name = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)
    date = models.DateField(null=True, blank=True)
    amount = models.IntegerField()
    class Meta:
        db_table='medicinedetails'
