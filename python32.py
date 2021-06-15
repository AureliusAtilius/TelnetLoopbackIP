import getpass
import telnetlib

HOST = "192.168.122.72" # Host we want to Telnet to
user = input("Enter your Telnet Username: ") # Prompt user for Telnet Username
password = getpass.getpass() # Prompt user for Telnet password
enablePW = getpass.getpass() # Prompt user for router enable password
tn = telnetlib.Telnet(HOST) # Initiate Telnet session to host

tn.read_until(b"Username: ") # Read Telnet output until you reach the Username prompt
tn.write(user.encode('ascii') + b"\n") # Input Username and carriage return
if password: # If password has been defined,
    tn.read_until(b"Password: ") # read output until Password prompt
    tn.write(password.encode('ascii') + b"\n") # input Password and carriage return

tn.write(b"enable\n") # input enable plus carriage return to elevate to privileged mode 
tn.write(enablePW.encode('ascii') + b"\n") # input enable password plus carriage return.
tn.write(b"conf t\n") # input "conf t" plus carriage return to enter global configuration mode.
tn.write(b"vlan 2\n") # Create VLAN 2
tn.write(b"name Python_VLAN_2\n") 
tn.write(b"vlan 3\n") # Create VLAN 3
tn.write(b"name Python_VLAN_3\n")
tn.write(b"vlan 4\n") # Create VLAN 4
tn.write(b"name Python_VLAN_4\n")
tn.write(b"vlan 5\n") # Create VLAN 5
tn.write(b"name Python_VLAN_5\n")
tn.write(b"end\n") # Exit global configuration mode
tn.write(b"exit\n") # Exit Telnet session

print(tn.read_all().decode('ascii'))