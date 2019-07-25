from django.db import models


class Uom(models.Model):
    uom = models.CharField(max_length=50)

    def __str__(self):
        return self.uom


class Item(models.Model):
    item_code = models.AutoField(primary_key=True)
    item_description = models.CharField(max_length=300)
    price = models.IntegerField()
    uom = models.ForeignKey(Uom, on_delete=models.CASCADE)

    def __str__(self):
        return self.item_description
