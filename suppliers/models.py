from django.db import models




class Supplier(models.Model):
    supplier_code = models.CharField(max_length=200, primary_key=True)
    company_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.supplier_code
