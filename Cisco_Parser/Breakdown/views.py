from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from Interface_Cisco_Configuration_Parser import interface_ciscoconfparse
from pathlib import Path
import requests
import os
import traceback
from openpyxl import Workbook
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

def Home_Page(request):
    return render(request, 'base.html')

def Parser_Page(request):
    return render(request, 'Parser_Page.html')

def delete_file():
    os.remove('/Users/praveenselvarajan/Desktop/Cisco_Parser/Cisco_Parser/media/interface_testing.csv')

def upload_read(request):
    running_configuration_list = []
    try:
        f = request.FILES['running_config']
        hostname,extension = f.name.split(".")
        uploaded_file_readlines_list = request.FILES['running_config'].readlines()
        for each_uploaded_file_readlines in uploaded_file_readlines_list:
            running_configuration_list += [each_uploaded_file_readlines.decode().strip("\n").strip("\r")]
        final_config = interface_ciscoconfparse.main(running_configuration_list)
        with open(os.path.join(BASE_DIR,'media/interface_testing.csv'), 'rb') as fq:
            data = fq.read()
        delete_file()
        response = HttpResponse(data, content_type='text/html; charset=UTF-8')
        response['Content-Disposition'] = 'attachment; filename='+hostname+'.csv'
        return response
        return render(request, 'Parser_Page.html')
    except Exception:
        traceback.print_exc()
        return render(request, 'Parser_Page.html')