from django.db import models

# Create your models here.
class Entry(models.Model):
    weight = models.FloatField()
    entry_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Weight: {self.weight} Date: {self.entry_date}'