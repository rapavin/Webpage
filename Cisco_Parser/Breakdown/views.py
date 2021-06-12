from django.shortcuts import render
from django.http import HttpResponse


def Home_Page(request):
    return render(request, 'base.html')

def Firmware_Page(request):
    return render(request, 'firmware_page.html')

def stacking_Page(request):
    return render(request, 'stacking_page.html')