from django.db import models

class History(models.Model):
    id =   models.IntegerField(primary_key=True, db_index=True)
    type = models.CharField(max_length=3)
    dt =models.DateTimeField()

    amount = models.FloatField()
    price = models.FloatField()