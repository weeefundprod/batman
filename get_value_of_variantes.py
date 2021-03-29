import os
import test
import json
import sys
import subprocess
import re
from math import *

#res = subprocess.check_output(['dmesg','stdout','egrep', '-i', '--color', '"cdrom|dvd|cd/rw|writer"'])
#cmd = "xdpyinfo | grep dimensions | sed -r 's/^[^0-9]*([0-9]+x[0-9]+).*$/\1/'"

# Opening JSON file 
f = open('mydata.json') 
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
vendor=data[0]['vendor']
print('Vendor: ',data[0]['vendor'])

product=data[0]['product']
print('Product: ',data[0]['product'])

serial_number=data[0]['serial']
print('Serial: ',data[0]['serial'])

if "sku" in data[0]['configuration']: 
    sku = data[0]['configuration']['sku']
else:
    sku = None


graphic_card= os.environ["GRAPHIC_CARD"]
print('Carte Graphique: ',graphic_card)

processor= os.environ["PROCESSOR"]
print('Processor: ', processor)

#screenArray = os.environ["SCREEN"].split('x')
#screen = sqrt(((int(screenArray[0]))**2) + ((int(screenArray[1]))**2))* 0.0104166667
#print('SCREEN: ', screen)

# change the round factor if you like
r = 1

screens = [l.split()[-3:] for l in subprocess.check_output(
    ["xrandr"]).decode("utf-8").strip().splitlines() if " connected" in l]

for s in screens:
    w = float(s[0].replace("mm", "")); h = float(s[2].replace("mm", "")); d = ((w**2)+(h**2))**(0.5)
    screen = str(round(d/25.4, r))
print('SCREEN: ', screen)

dvd=os.environ["DVD"]
print('DVD: ', os.environ["DVD"])

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

# Closing file 
f.close()

#hhdssd = os.environ["HHDSSD"][0]
#print('HHDSSD: ', hhdssd)
#searching ssd
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
multimedia = open('multimedia.json')
datamultimedia= json.load(multimedia)
webcam = 'NULL'
for i in datamultimedia:
    if re.search('webcam', i['product'] , re.IGNORECASE): webcam = i['product']
multimedia.close()
print('Webcam :', webcam)

#searching bluetooth
print('bluetooth: ', os.environ["BLUETOOTH"])
bluetooth=os.environ["BLUETOOTH"]

print('Out python')