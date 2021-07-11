import textfsm
import os
import csv

def cisco_service_parser(reading_running_conf_read_string):
	global switch_data
	'''Find the location directory of the templates. Currently located at "textfsm_templates"'''
	switch_data = {}
	textfsm_templates_list = os.listdir("/home/ec2-user/webpage/Cisco_Parser/Cisco_Configuration_Parser/textfsm_templates")

	for each_textfsm_templates_list in textfsm_templates_list:
		with open("/home/ec2-user/webpage/Cisco_Parser/Cisco_Configuration_Parser/textfsm_templates/"+each_textfsm_templates_list) as all_textfsm_templates:
			regex_table_fsm_data = textfsm.TextFSM(all_textfsm_templates)
			data = regex_table_fsm_data.ParseText(reading_running_conf_read_string)
			try:
				if len(data)==1:
					switch_data[each_textfsm_templates_list[0:-4]] = data[0]
				elif len(data)==0:
					switch_data[each_textfsm_templates_list[0:-4]] = ["N/A"]
				elif len(data)>1:
					switch_data[each_textfsm_templates_list[0:-4]] = data
			except:
				pass
	with open('/home/ec2-user/webpage/Cisco_Parser/TEMP_FILE_STORAGE/interface_testing.csv', 'w+', newline='') as services_csv_file:
		writer = csv.writer(services_csv_file)
		writer.writerow(["HOSTNAME",switch_data['cisco_show_run_hostname'][0]])
		writer.writerow(["SPANNING TREE MODE",switch_data['cisco_show_run_spanning_tree_mode'][0]])
		#writer.writerow(["VERSION",switch_data['cisco_show_run_version'][0]])
		writer.writerow(["BOOT SYSTEM",switch_data['cisco_show_run_boot_system'][0]])
		writer.writerow(["ENABLE",switch_data['cisco_show_run_enable_secret'][0]])
		writer.writerow(["VTP MODE",switch_data['cisco_show_run_vtp_mode'][0]])
		writer.writerow(["VTP DOMAIN",switch_data['cisco_show_run_vtp_domain'][0]])
		writer.writerow(["DOMAIN NAME",switch_data['cisco_show_run_ip_domain_name'][0]])
		if len(switch_data['cisco_show_run_ntp'])>1:
			writer.writerow([""])
			for each_switch_data in switch_data['cisco_show_run_ntp']:
				writer.writerow(["NTP",each_switch_data[0]])
			else:
				pass
			
		if len(switch_data['cisco_show_run_aaa'])>1:
			writer.writerow([""])
			for each_switch_data in switch_data['cisco_show_run_aaa']:
				writer.writerow(["AAA",each_switch_data[0]])
			else:
				pass
			
		if len(switch_data['cisco_show_run_logging'])>1:
			writer.writerow([""])
			for each_switch_data in switch_data['cisco_show_run_logging']:
				writer.writerow(["LOGGING",each_switch_data[0]])
			else:
				pass
			
		if len(switch_data['cisco_show_run_clock'])>1:
			writer.writerow([""])
			for each_switch_data in switch_data['cisco_show_run_clock']:
				writer.writerow(["CLOCK INFORMATION",each_switch_data[0]])
			else:
				pass
			
		if len(switch_data['cisco_show_run_service'])>1:
			writer.writerow([""])
			for each_switch_data in switch_data['cisco_show_run_service']:
				writer.writerow(["SERVICES",each_switch_data[0]])
			else:
				pass

		if len(switch_data['cisco_show_run_snmp'])>1:
			writer.writerow([""])
			for each_switch_data in switch_data['cisco_show_run_snmp']:
				writer.writerow(["SNMP",each_switch_data[0]])
			else:
				pass	
if __name__ == "__main__":
	main()

