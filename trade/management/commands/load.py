from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from trade.models import History

import json
import requests
import datetime
import time
import logging
import sys, traceback
from django.conf import settings

# Get an instance of a logger

logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s', level = logging.DEBUG, filename = u'/var/log/trade.log')

pair="btc_usd"
wait_sec=100

limit=2000


class Command(BaseCommand):

    def add_log(self, message):
        self.stdout.write(self.style.SUCCESS(message))
        logging.debug(message)

    def add(self, pair):
        add_count = 0
        try:
            response = requests.get('https://btc-e.nz/api/3/trades/%s?limit=%d' % (pair,limit))
        except:
            self.add_log('Equest error')
            self.add_log(traceback.print_exc(file=sys.stdout))

            time.sleep(wait_sec)
            self.add()

        json_data = json.loads(response.text)[pair]

        for curr in json_data:
            serious_price = getattr(settings, "SERIOUS_PRICE", 30000)

            price=curr['price']
            amount = float(curr['amount'])
            total=price*amount

            id = int(curr['tid'])

            dt = datetime.datetime.fromtimestamp(curr['timestamp'])
            dt = timezone.make_aware(dt, timezone.get_current_timezone())

            if total<serious_price:
                continue

            res = History.objects.filter(id=id)
            if len(res) == 0:
                h = History(id=id, type=curr['type'], price=price, amount=amount, dt=dt, pair=pair)
                h.save()

                add_count += 1

        if add_count>0:
            self.add_log('Pair %s Successfully addes %d records' % (pair,add_count))

        #time.sleep(wait_sec)
        #self.add()

    def handle(self, *args, **options):
        self.add('btc_usd')
        self.add('ltc_usd')
        self.add('nmc_usd')
        self.add('nvc_usd')
        self.add('ppc_usd')
        self.add('dsh_usd')
        self.add('eth_usd')

