#!/usr/bin/env python
ipaddress = input("Please enter an IP Address: ")
ipaddress = ipaddress.split(".")
print(f"{ipaddress[0]:<12}, {ipaddress[1]:<12}, {ipaddress[2]:<12}, {ipaddress[3]:<12}")
