import os
import test
import json
import sys
import subprocess
import re
import csv
import sqlite3
from sqlite3 import Error
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

serial=data[0]['serial']
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

print('DVD: ', os.environ["DVD"])
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

#ssd (donnees introuvables sur PC lisa)
#print(data[0]['children'][0]['children'][4]['children'][12]['children'][0]['product'])

#webcam (donnees introuvables)
#print(data[0]['children'][0]['children'][4]['children'][10]['children'][0]['children'][0]['children'][0]['product'])



#searching Webcam
multimedia = open('multimedia.json')
datamultimedia= json.load(multimedia)
webcam = 'NULL'
for i in datamultimedia:
    if re.search('webcam', i['product'] , re.IGNORECASE): webcam = i['product']
multimedia.close()
print('Webcam :', webcam)

#searching bluetooth
# communicationjson = open('communication.json')
# communication= json.load(communicationjson)
# bluetooth = 'NULL'
# for i in communication:
#     if re.search('bluetooth', i['description'] , re.IGNORECASE): bluetooth = i['description']
# multimedia.close()
# print('Bluetooth :', bluetooth)
print('bluetooth: ', os.environ["BLUETOOTH"])
bluetooth=os.environ["BLUETOOTH"]


#csv_file = open("weefundinventory.csv", "w")

#with open('weeefundInventory.csv','a') as fd:
#    fd.write(str(serial, product))

# data = [(serial,product,sku,vendor,screen,ram,hhdssd,graphic_card,webcam,bluetooth,dvd)]
# df = pd.DataFrame(data)

# # if file exists....
# if os.path.isfile('weeefundInventory.csv'):
#     #Old data
#     oldFrame = pd.read_csv('weeefundInventory.csv')
#     #oldFrame.columns = oldFrame.iloc[0]
#     #print(oldFrame.columns)

#     #Concat
#     df_diff = pd.concat([oldFrame, df],ignore_index=True).drop_duplicates()

#     #Write new rows to csv file
#     df_diff.to_csv('weeefundInventory.csv', header=False, index=False)

# else: # else it exists so append
#     df.to_csv('weeefundInventory.csv', header=False, index=False)



# def sql_connection():

#     try:

#         con = sqlite3.connect('./weeefundDatabase')

#         print("Connection is established: Database is created in memory")
#         cursor = con.cursor()
#         cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#         cursor.execute("SELECT SERIAL_NUMBER, MODEL from product")
#         rows = cursor.fetchall()
#         print('rows',rows)
#         alreadyExits = False
#         for row in rows:
#             print('row', row)
#             if row[0] == serial:
#                 if row[1] == product:
#                     print("Le serial number existe deja")
#                     alreadyExits = True
                    
#         if not rows:
#             alreadyExits = False

#         if alreadyExits == False:
#             try:
#                 sql = "INSERT INTO product (SERIAL_NUMBER, MODEL, SKU, VENDOR, SCREEN, HHD_SSD, GRAPHIC_CARD, WEBCAM, BLUETOOTH, DVD) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
#                 val = (serial, product, sku, vendor, screen, hhdssd, graphic_card, webcam, bluetooth, dvd)
#                 #cursor.execute("INSERT INTO product (SERIAL_NUMBER, MODEL, SKU, VENDOR, SCREEN, HHD_SSD, GRAPHIC_CARD, WEBCAM, BLUETOOTH, DVD) VALUES('testldf', 'test', 'test', 'test', 'test', 'test','test', 'test', 'test', 'test')")
#                 cursor.execute( sql,val)
#                 print("Entree en base")
#             except sqlite3.Error as er:
#                 print('Not insert in database:', er)

#             try:
#                 #Retrieve data
#                 cursor.execute("SELECT * FROM product")
#                 rows = cursor.fetchall()
#                 for row in rows:
#                     print(row)

#             except sqlite3.Error as er:
#                 print('error:', er.message)

#         con.commit()

#     except Error:

#         print( Error)

#     finally:

#         con.close()

# sql_connection()

print('Out python')