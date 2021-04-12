from get_value_of_variantes import *
import sqlite3
from sqlite3 import Error


try:
    con = sqlite3.connect('./weeefundDatabase')
    print("Connection etablie avec la database interne")
    cursor = con.cursor()
    cursor.execute("SELECT SERIAL_NUMBER, MODEL from product")
    rows = cursor.fetchall()

    alreadyExits = False
    for row in rows:
        if row[0] == serial_number:
            if row[1] == product:
                print("Le serial number existe deja dans la database interne")
                alreadyExits = True
    if not rows:
        alreadyExits = False

    if alreadyExits == False:
        try:
            sql = "INSERT INTO product (SERIAL_NUMBER, MODEL, SKU, VENDOR, SCREEN, HHD_SSD, GRAPHIC_CARD, WEBCAM, BLUETOOTH, DVD, INTERNAL_NUMBER) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            val = (serial_number, product, sku, vendor, screen, ', '.join(array_hhd_sdd), graphic_card, webcam, bluetooth, dvd, internal_number)
            cursor.execute( sql,val)
            print("Entree en base du produit ", product, "serial number", serial_number)
        except sqlite3.Error as er:
            print('Error insert in database:', er)

    con.commit()
except Error:
    print('Error from sql requests', Error)
finally:
    con.close()