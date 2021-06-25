from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from Interface_Cisco_Configuration_Parser import interface_ciscoconfparse
from Cisco_Configuration_Parser import cisco_conf_parser
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
    os.remove('/home/ec2-user/webpage/Cisco_Parser/TEMP_FILE_STORAGE/interface_testing.csv')

def convert_each_uploaded_file_readlines_to_string():
    str1 = "" 
    for each_running_configuration_list in running_configuration_list: 
        str1 += each_running_configuration_list
    return str1
            
def upload_read(request):
    global running_configuration_list
    running_configuration_list = []
    try:
        f = request.FILES['running_config']
        hostname,extension = f.name.split(".")
        uploaded_file_readlines_list = request.FILES['running_config'].readlines()
        for each_uploaded_file_readlines in uploaded_file_readlines_list:
            running_configuration_list += [each_uploaded_file_readlines.decode().strip("\n").strip("\r")]
        final_config = interface_ciscoconfparse.main(running_configuration_list)
        running_configuration_list_read = convert_each_uploaded_file_readlines_to_string()
        services_templates = cisco_conf_parser.import_textfsm_template(running_configuration_list_read)
        cisco_conf_parser.convert_services_result_csv()
        f = open("services_config.csv", "r")
        print(type(f))
        encoded_string = f.encode()
        byte_array = bytearray(encoded_string)
        print(byte_array)
        print(type(byte_array))
        print(os.listdir())
        with open(os.path.join(BASE_DIR,'TEMP_FILE_STORAGE/interface_testing.csv'), 'rb') as fq:
            data_bytes = fq.read()
        final_bytes = byte_array+data_bytes
        delete_file()
        response = HttpResponse(final_bytes, content_type='text/html; charset=UTF-8')
        response['Content-Disposition'] = 'attachment; filename='+hostname+'.csv'
        return response
        return render(request, 'Parser_Page.html')
    except Exception:
        traceback.print_exc()
        return render(request, 'Parser_Page.html')
