from django.http import HttpResponse
from django.shortcuts import render

def test_print(request):
    return HttpResponse("TEST MESSAGE")
