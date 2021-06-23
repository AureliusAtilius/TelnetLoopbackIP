import getpass, telnetlib
from os import read

# Collect Telnet credentials
user = input("Enter your Telnet Username: ")
password = getpass.getpass()

# Read through list of IP addresses and Telnet to each
f = open('myswitches')

for IP in f:
        IP = IP.strip()
        print("Get running config from Switch "+(IP))
        HOST = IP
        tn = telnetlib.Telnet(HOST)
        tn.read_until(b'Username: ')
        tn.write(user.encode('ascii')+b'\n')
        # Have terminal print all lines of running config
        tn.write(b"terminal length 0\n")
        tn.write(b"show run\n")

        # Read the terminal out put and save it to a file.
        readoutput= tn.read_all()
        saveoutput= open("switch"+HOST, "w")
        saveoutput.write(read.decode('ascii'))
        saveoutput.write("\n")
        saveoutput.close
        print(tn.read_all().decode('ascii'))
