# import built-in os library
# https://docs.python.org/3/library/os.html
import os

# List of string ip addresses to ping
ip_list = ["8.8.8.8", "8.8.4.4", "this is unsuccessful"]

# Loop to ping ip_list to check if device up or down
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        print(f"UP {ip} Ping Successful")
    else:
        print(f"Down {ip} Ping Unsuccessful")
