from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from Interface_Cisco_Configuration_Parser import interface_ciscoconfparse
from Cisco_Configuration_Parser import cisco_conf_parser
from pathlib import Path
import requests
import csv
import os
import traceback
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

def Home_Page(request):
    return render(request, 'base.html')

def Parser_Page(request):
    return render(request, 'Parser_Page.html')

def delete_file():
    os.remove('/home/ec2-user/webpage/Cisco_Parser/TEMP_FILE_STORAGE/interface_testing.csv')

def convert_each_uploaded_file_readlines_to_string(list_variable):
    str1 = "" 
    for each_running_configuration_list in list_variable: 
        str1 += each_running_configuration_list
    return str1

def upload_read(request):
    global running_configuration_list
    running_configuration_list = []
    try:
        f = request.FILES['running_config']
        print(f)
        print(type(f))
        hostname,extension = f.name.split(".")
        uploaded_file_readlines_list = request.FILES['running_config'].readlines()
        #print(uploaded_file_readlines_list)
        for each_uploaded_file_readlines in uploaded_file_readlines_list:
            running_configuration_list += [each_uploaded_file_readlines.decode().strip("\n").strip("\r")]
        final_config = interface_ciscoconfparse.main(running_configuration_list)
        running_configuration_list_read = convert_each_uploaded_file_readlines_to_string(running_configuration_list)
        print(running_configuration_list_read)
        #print(running_configuration_list_read)
        #print(type(running_configuration_list_read))
        services_templates = cisco_conf_parser.import_textfsm_template(running_configuration_list_read)
        #print(type(services_templates))
        #cisco_conf_parser.convert_services_result_csv()
        
        #f = open('services_config.csv', 'w+')
        #f_read = f.read()
        #print(f_read)
        #writer = csv.writer(f)
        #writer.writerow(f_read)
        #writer.writerow(["\n"*10])

        #with open(os.path.join(BASE_DIR,'services_config.csv'), 'rb') as service_read_bytes:
        #    service_bytes = service_read_bytes.read()
        #print(service_bytes)
        #print(type(service_bytes))
        with open(os.path.join(BASE_DIR,'TEMP_FILE_STORAGE/interface_testing.csv'), 'rb') as fq_read_bytes:
            data_bytes = fq_read_bytes.read()
        #print(data_bytes)
        #print(type(data_bytes))
        #print(type(data_bytes))
        delete_file()
        response = HttpResponse(data_bytes, content_type='text/html; charset=UTF-8')
        response['Content-Disposition'] = 'attachment; filename='+hostname+'.csv'
        return response
        return render(request, 'Parser_Page.html')
    except Exception:
        return render(request, 'Parser_Page.html')
