from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    piece = models.IntegerField(default=0)
    img_path = models.CharField(max_length=255)
    description = models.CharField(max_length=400)
    in_cart = models.BooleanField(default=False)

    @property
    def total(self):
        total = self.piece * self.price
        total = round(total, 2)
        return total
