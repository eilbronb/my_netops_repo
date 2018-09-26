import pexpect,re

username = "ignw"
password = "ignw"
device_ip = "10.0.0.5"

connection = pexpect.spawn(f"ssh {username}@{device_ip}")

connection.expect("Password:")
connection.sendline(password)

print (connection.before)
print (connection.after)

connection.expect("ignw-csr#")

connection.sendline("show run intergace g1")
connection.expect("ignw-csr#")

interface_output(connection.before)
print(interface_output)
