from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from Interface_Cisco_Configuration_Parser import interface_ciscoconfparse
from pathlib import Path
import requests

def Home_Page(request):
    return render(request, 'base.html')

def Parser_Page(request):
    return render(request, 'Parser_Page.html')

def file_move():
    Path("/Users/praveenselvarajan/Desktop/Cisco_Parser/Cisco_Parser/interface_testing.csv").rename("/Users/praveenselvarajan/Desktop/Cisco_Parser/Cisco_Parser/media/interface_testing.csv")

def upload_read(request):
    running_configuration_list = []
    f = request.FILES['running_config']
    uploaded_file_readlines_list = request.FILES['running_config'].readlines()

    for each_uploaded_file_readlines in uploaded_file_readlines_list:
        running_configuration_list += [each_uploaded_file_readlines.decode().strip("\n").strip("\r")]

    final_config = interface_ciscoconfparse.main(running_configuration_list)
    file_move()

    #http://127.0.0.1:8000/media/interface_testing.csv

    return render(request, 'Parser_Page.html')