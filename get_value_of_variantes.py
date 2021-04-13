#!/usr/bin/python3
import os
import test
import json
import sys
import subprocess
import re
from math import *
import xml.etree.ElementTree as ET
import shortuuid


#res = subprocess.check_output(['dmesg','stdout','egrep', '-i', '--color', '"cdrom|dvd|cd/rw|writer"'])

  
vendor=os.environ["VENDOR"]

product=os.environ["PRODUCT"]


bluetooth=os.environ["BLUETOOTH"]

if not os.environ["SKU"]: 
    sku = os.environ["SKU"]
else:
    sku = None


graphic_card= os.environ["GRAPHIC_CARD"]

processor= os.environ["PROCESSOR"]

serial_number=os.environ["SERIAL_NUMBER"]

# change the round factor if you like
r = 1

screens = [l.split()[-3:] for l in subprocess.check_output(
    ["xrandr"]).decode("utf-8").strip().splitlines() if " connected" in l]

for s in screens:
    w = float(s[0].replace("mm", "")); h = float(s[2].replace("mm", "")); d = ((w**2)+(h**2))**(0.5)
    screen = str(round(d/25.4, r))

dvd=os.environ["DVD"]

ram_no_split=os.environ["RAM"]
ram_split = float(ram_no_split.split('Gi')[0].replace(",", "."))
if 0 <= ram_split <= 2:
    ram= '2Go'
elif 2 <= ram_split <= 4:
    ram= '4Go'
elif 4 <= ram_split <= 8:
    ram= '8Go'
elif 8 <= ram_split <= 16:
    ram= '16Go'
elif 16 <= ram_split <= 24:
    ram= '24Go'
elif 24 <= ram_split <= 32:
    ram= '32Go'
elif 32 <= ram_split <= 64:
    ram= '64Go'
elif 64 <= ram_split <= 128:
    ram= '128Go'
elif 12 <= ram_split <= 256:
    ram= '256Go'


# get hhd sdd
tree = ET.parse(serial_number+'.xml')
disk_xml = tree.getroot()

variableDesc = False
variableSerial =""
array_hhd_sdd = []
array_id_hhd_sdd = []
for child in disk_xml:
    for s in child:
        if (s.tag == "description") and (s.text == "ATA Disk"):
            variableDesc = True
        if  (variableDesc == True) and (s.tag == "serial"):
            variableSerial = s.text
            array_id_hhd_sdd.append(variableSerial)
        if  (variableDesc == True) and (s.tag == "product"):
            hhd_sdd = s.text
            array_hhd_sdd.append(hhd_sdd)
    variableDesc = False



#searching Webcam
webcam=os.environ["WEBCAM"]


#searching bluetooth
bluetooth=os.environ["BLUETOOTH"]

enterprise=os.environ["ENTERPRISE"]

internal_number=os.environ["NUMERO_LOT"]+shortuuid.ShortUUID().random(length=3)+'-'+enterprise