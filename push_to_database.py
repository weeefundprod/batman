from get_value_of_variantes import *
import sqlite3
from sqlite3 import Error


print("push to database")

try:
    con = sqlite3.connect('./weeefundDatabase')
    print("Connection is established: Database is created in memory")
    cursor = con.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    cursor.execute("SELECT SERIAL_NUMBER, MODEL from product")
    rows = cursor.fetchall()

    alreadyExits = False
    for row in rows:
        if row[0] == serial_number:
            if row[1] == product:
                print("Le serial number existe deja")
                alreadyExits = True
    if not rows:
        alreadyExits = False

    if alreadyExits == False:
        try:
            sql = "INSERT INTO product (SERIAL_NUMBER, MODEL, SKU, VENDOR, SCREEN, HHD_SSD, GRAPHIC_CARD, WEBCAM, BLUETOOTH, DVD) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            val = (serial_number, product, sku, vendor, screen, hhdssd, graphic_card, webcam, bluetooth, dvd)
            cursor.execute( sql,val)
            print("Entree en base")
        except sqlite3.Error as er:
            print('Error insert in database:', er)

    con.commit()
except Error:
    print('Error from sql requests', Error)
finally:
    con.close()