from django.db import models
from django.db.models import Max


class History(models.Model):
	id =   models.IntegerField(primary_key=True, db_index=True)
	type = models.CharField(max_length=3)
	dt =models.DateTimeField()

	amount = models.FloatField()
	price = models.FloatField()
	pair = models.CharField(max_length=7,  default='btc_usd')

class Orders(models.Model):
	id = models.IntegerField(primary_key=True)

	pair = models.CharField(max_length=7)
	type=models.CharField(max_length=7)
	amount = models.FloatField()
	rate = models.FloatField()
	dt =models.DateTimeField()

	linked_order = models.ForeignKey(History)





