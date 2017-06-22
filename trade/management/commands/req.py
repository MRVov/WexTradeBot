from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from trade.models import History
from trade.models import Requests
from ...btceapi import api as btc_api

import json
import requests
import datetime
import time
import logging
import sys, traceback


class calc_indicators():
	def __init__(self, history_id):
		pass


class Command(BaseCommand):

	def handle(self, *args, **options):
		tpair='btc_usd'

		__api_key = 'MIM5CS0R-BEL2S73E-TSRKG8K2-SMUWMCEL-QFKB3R9U'
		__api_secret = 'c901a5d8d99eb70536af9fcc588f4a08197a877745c78e9e00defc109b6c41ef'

		api=btc_api(__api_key, __api_secret, wait_for_nonce=True)
		res=api.ActiveOrders(tpair)
		self.stdout.write(self.style.SUCCESS(str(res)))


