import time,sys
from netmiko import ConnectHandler


cisco_cloud_nxos = {'device_type':'cisco_nxos',
			'ip':'10.0.0.6',
			'username':'ignw',
			'password':'ignw'
			}
connection = ConnectHandler(**cisco_cloud_nxos)

configuration = ['feature interface-vlan','vlan 1000','interface vlan 1000',
'des to ASAv','ip address 10.255.255.2 255.255.255.240','no shut','int eth1/2',
'switchport','no shut','switchport mode trunk',
'switchport trunk native vlan 1000','no shut']

output1 = connection.send_config_set(configuration)
time.sleep(2)

show_output = connection.send_command('show ip int brief | i Vlan1000')
if show_output.count('up') == 3:
	print ('It looks like Vlan1000 is up/up! vlan')
else:
	print ('Something went wrong, vlan')
	sys.exit()
show_output = connection.send_command('show int status | i Eth1/2')
if show_output.count('connected') == 1:
	print('It looks like Eth1/2 is up/up port!')
else:
	print('Something went wrong, port')
	sys.exit()

