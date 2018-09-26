from netmiko import ConnectHandler

cisco_cloud_router = {'device_type':'cisco_ios',
			'ip':'10.0.0.5',
			'username':'ignw',
			'password':'ignw'}

connection = ConnectHandler(**cisco_cloud_router)

interface_output = connection.send_command('show run int g1')
hostname = connection.find_prompt()
interface_name = connection.send_command('show run int g1 | i ^interface')
ip_output = connection.send_command('show run int g1 | i ip address')
if 'no' in  ip_output:
	interface_ip_address = []
	interface_ip_address[0] = 'N/A'
else:
	interface_ip_address = []
	for line in  ip_output.split('\n'):
		interface_ip_address.append(line[12:])
#print(interface_output)
#print(hostname[:-1])
#print(interface_name)
print(interface_ip_address)


