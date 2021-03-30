import os
import test
import json
import sys
import subprocess
import re
from math import *

print("get value")
#res = subprocess.check_output(['dmesg','stdout','egrep', '-i', '--color', '"cdrom|dvd|cd/rw|writer"'])

  
vendor=os.environ["VENDOR"]
print('Vendor: ',vendor)

product=os.environ["PRODUCT"]
print('Product: ',product)


bluetooth=os.environ["BLUETOOTH"]
print('bluetooth: ', bluetooth)

if not os.environ["SKU"]: 
    sku = os.environ["SKU"]
else:
    sku = None
print('sku: ', sku)


graphic_card= os.environ["GRAPHIC_CARD"]
print('Carte Graphique: ',graphic_card)

processor= os.environ["PROCESSOR"]
print('Processor: ', processor)

# change the round factor if you like
r = 1

screens = [l.split()[-3:] for l in subprocess.check_output(
    ["xrandr"]).decode("utf-8").strip().splitlines() if " connected" in l]

for s in screens:
    w = float(s[0].replace("mm", "")); h = float(s[2].replace("mm", "")); d = ((w**2)+(h**2))**(0.5)
    screen = str(round(d/25.4, r))
print('SCREEN: ', screen)

dvd=os.environ["DVD"]
print('DVD: ', dvd)

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
print('RAM: ', ram)


hhdssd = list()
diskjson= open('disk.json')
disk= json.load(diskjson)
for i in disk:
	if i['description'] == 'ATA Disk':
    		hhdssd.append(i['serial'])
diskjson.close()
diskjson.close()
print('HHDSSD: ', hhdssd)

#searching Webcam
webcam=os.environ["WEBCAM"]
print('Webcam: ', webcam)


#searching bluetooth
bluetooth=os.environ["BLUETOOTH"]
print('bluetooth: ', bluetooth)

serial_number=os.environ["SERIAL_NUMBER"]
print('Serial Number: ', serial_number)

print('Out python')