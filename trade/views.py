# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.views.generic.edit import FormView,View
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.http import HttpResponseRedirect,HttpResponse


from .models import *

from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

from django.views.decorators.http import require_POST

from django.http import JsonResponse
from django.http import HttpResponseForbidden
from django.forms import ModelForm
from django.db.models import Q


from django.shortcuts import render
import json

@login_required
def order(request, order_id):
    return render(request, 'managers/order.html', {
    })
