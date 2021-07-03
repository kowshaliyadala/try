#from django.http import JsonResponse
from django.shortcuts import render
#import json

# Create your views here.


#def products(request):

    #with open('productDB.json', 'r') as f:
        #product = json.load(f)
        #return JsonResponse({'status': True, 'product': product})


import json
from django.conf import settings
from django.http import JsonResponse
import re


def product(request):
    if request.method == 'POST':
        data = request.body
        settings.PRODUCT_COLLECTION.insert_one(data)
    return JsonResponse({'status': True})


