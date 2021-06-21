import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your remote account: ")
password = getpass.getpass()

# Read list of IP addresses and telnet to each switch.
f = open ('myswitches')

for IP in f:
   IP=IP.strip()
   print ("Configuring Switch " + (IP))
   HOST = IP
   tn = telnetlib.Telnet(HOST)
   tn.read_until(b"Username: ")
   tn.write(user.encode('ascii') + b"\n")
   
   # Login to switch
   if password:
       tn.read_until(b"Password: ")
       tn.write(password.encode('ascii') + b"\n")
   tn.write(b"conf t\n")

   # Create and name VLANs 2-20
   for i in range(2,21):
      tn.write(b"vlan " + str(i).encode('ascii') + b"\n")
      tn.write(b"name  Python_VLAN_"+str(i).encode('ascii')+b"\n")

   # Exit global config mode
   tn.write(b"end\n")
   tn.write(b"exit\n")
   print(tn.read_all().decode('ascii'))