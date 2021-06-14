import getpass
import telnetlib

HOST = "192.168.122.71" # Host we want to Telnet to
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
tn.write(b"int loop 0\n") # enter interface configuration mode for loopback interface 0
tn.write(b"ip address 1.1.1.1 255.255.255.255\n") # Configure ip address for loopback int 0
tn.write(b"end\n") # Exit global configuration mode
tn.write(b"exit\n") # Exit Telnet session

print(tn.read_all().decode('ascii'))