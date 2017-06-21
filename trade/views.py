# -*- coding: utf-8 -*-


from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from matplotlib.pylab import *
from matplotlib import pylab
import PIL
from  PIL import Image
import io
from io import *
from PIL import Image

import matplotlib.pyplot as plt
from pandas import date_range,Series,DataFrame,read_csv, qcut
from pandas.tools.plotting import radviz,scatter_matrix,bootstrap_plot,parallel_coordinates
from numpy.random import randn
from pylab import *
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter
from django.conf import settings


from matplotlib import rcParams
from trade.models import History
import pandas as pd

import random
INK = "red", "blue", "green", "yellow"

from django.shortcuts import render
import json

@login_required
def order(request, order_id):
    return render(request, 'managers/order.html', {
    })

def graphic(request, pair, period):
    serious_price=getattr(settings, "SERIOUS_PRICE", 30000)

    days=int(period)
    today = datetime.date.today()
    days_ago = today - datetime.timedelta(days=days)

    vals=History.objects.all().filter(pair=pair).filter(dt__gte=days_ago).order_by('dt')

    print len(vals)

    ddt_arr=[]
    b_amount_arr=[]
    a_amount_arr=[]

    price_arr=[]

    for curr in vals:
        total=curr.amount*curr.price

        if total<serious_price:
            continue

        dt=curr.dt
        dt=dt.replace(tzinfo=None)
        ddt_arr.append(dt)

        if curr.type=='bid':
            b_amount_arr.append(curr.amount)
            a_amount_arr.append(None)
        else:
            a_amount_arr.append(curr.amount)
            b_amount_arr.append(None)

        price_arr.append(curr.price)

    fig = Figure()

    ax = fig.add_subplot(211)
    ax.plot_date(ddt_arr, a_amount_arr, 'r^' )
    ax.plot_date(ddt_arr, b_amount_arr, 'b^')

    ax = fig.add_subplot(212)
    ax.plot_date(ddt_arr, price_arr, '-' )

    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d %H'))
    fig.autofmt_xdate()
    canvas = FigureCanvas(fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response