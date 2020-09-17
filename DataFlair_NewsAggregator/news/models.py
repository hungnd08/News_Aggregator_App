from django.db import models

# Create your models here.
class Headline(models.Model):
    title = models.CharField(max_length=200)
    image = models.URLField(null=True, blank=True)
    original_price = models.CharField(null=True, max_length=50)
    promotional_price = models.CharField(null=True, max_length=50)
    url = models.TextField()

    def __str__(self):
        return self.title

    def get_original_price(self):
        if self.original_price != None:
            return self.original_price
        return ""

    def get_promotional_price(self):
        if self.promotional_price != None:
            return self.promotional_price
        return ""
