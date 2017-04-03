from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone

from trade.models import History

import json
import requests
import datetime
import time


pair="btc_usd"
wait_sec=10
min_amount=0.85

class Command(BaseCommand):
    def add(self):
        add_count = 0
        try:
            response = requests.get('https://btc-e.nz/api/3/trades/btc_usd')
        except:
            self.stdout.write(self.style.SUCCESS('Equest error ' ))
            time.sleep(20)
            self.add()

        json_data = json.loads(response.text)['btc_usd']

        for curr in json_data:
            dt = datetime.datetime.fromtimestamp(curr['timestamp'])
            dt = timezone.make_aware(dt, timezone.get_current_timezone())
            amount=float(curr['amount'])

            if amount<min_amount:
                continue

            id = int(curr['tid'])

            res = History.objects.filter(id=id)
            if len(res) == 0:
                h = History(id=id, type=curr['type'], price=curr['price'], amount=amount, dt=dt)
                h.save()
                add_count += 1

        if add_count>0:
            self.stdout.write(self.style.SUCCESS('Successfully addes %d records' % add_count))

        time.sleep(wait_sec)
        self.add()

    def handle(self, *args, **options):
        self.add()
