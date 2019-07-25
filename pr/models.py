from django.db import models
from suppliers.models import Supplier
from items.models import Item
from datetime import datetime


class PRHead(models.Model):
    pr_no = models.IntegerField(primary_key=True)
    pr_date = models.DateField(default=datetime.now)
    approved_date = models.DateField(default=datetime.now)

    class Meta:
        ordering = ('pr_no',)

    def __str__(self):
        return str(self.pr_no)


class PRDetail(models.Model):
    pr_head = models.ForeignKey(PRHead, on_delete=models.CASCADE)
    item = models.ForeignKey(to=Item, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    amount = models.IntegerField()
    tax = models.IntegerField()

    class Meta:
        unique_together = (('pr_head', 'item'),)

    def __str__(self):
        return str(self.pr_head) + " | " + str(self.pr_head.pr_date)
