#Collect logs (of any kind) and write a parser which pulls out specific details (domains, executable names, timestamps etc.)

#Pull IP addresses, time stamps, and endpoints from log files 

#Helpful resource: https://regexr.com

import re

lines = ""
with open('access.log') as f:
    lines = f.readlines()
    for line in lines:

       ip_addresses = re.findall( r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', str(line))

       time_stamps = re.findall( r'(?:\d{4}\:)(\d\d:\d\d:\d\d)', str(line))
    
       z = str(line)
       z = z.replace("\n","")
       z = z.replace("\"","")
       endpoints = re.findall("(?:\w\w\w\w?)( \/.*)(?:.HTTP)", z)

       if len(ip_addresses) > 0 and len(time_stamps) > 0 and len(endpoints) > 0:
           print (ip_addresses[0],time_stamps[0],endpoints[0])





