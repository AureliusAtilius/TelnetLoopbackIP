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

# Create VLANS 2-20
for i in range(2,21):

    tn.write(b"vlan " + str(i).encode('ascii') + b"\n")
    tn.write(b"name  Python_VLAN_"+str(i).encode('ascii')+b"\n")

tn.write(b"end\n") # Exit global configuration mode
tn.write(b"wr\n")  # Save configuration
tn.write(b"exit\n") # Exit Telnet session

print(tn.read_all().decode('ascii'))