from netmiko import ConnectHandler

cisco_cloud_router = {'device_type':'cisco_ios',
			'ip':'10.0.0.5',
			'username':'ignw',
			'password':'ignw'
			}

connection = ConnectHandler(**cisco_cloud_router)

configuration = ['interface GigabitEthernet2', 'ip address 203.0.113.1 255.255.255.192',
		'des outside', 'no shut']
route_config = ['ip route 10.255.255.2 255.255.255.255 203.0.113.2']
#output1 = connection.send_config_set(configuration)
output2 = connection.send_command('show ip route')
output3 = connection.send_config_set(route_config)
#print(output1)
print(output2)
