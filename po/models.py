from django.db import models
from suppliers.models import Supplier
from items.models import Item
from datetime import datetime


class POHead(models.Model):
    po_no = models.IntegerField(primary_key=True)
    po_date = models.DateField(default=datetime.now)
    approved_date = models.DateField(default=datetime.now)

    class Meta:
        ordering = ('po_no',)

    def __str__(self):
        return str(self.po_no)


class PODetail(models.Model):
    po_head = models.ForeignKey(POHead, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.IntegerField()
    tax = models.IntegerField()

    class Meta:
        unique_together = (('po_head', 'item'),)
        ordering = ('po_head',)

    def __str__(self):
        return str(self.po_head) + " | " + str(self.item)
