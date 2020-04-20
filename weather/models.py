from django.db import models

class weath(models.Model):
    city = models.CharField(max_length = 25)
    def __str__(self):
        return self.city
