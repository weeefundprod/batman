import sqlite3

from sqlite3 import Error

        # sql = "INSERT INTO product VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # val = (serial, product, sku, vendor, screen, hhdssd, graphic_card, webcam, bluetooth, dvd)
        # cursor.execute(sql, val)
    sql = "INSERT INTO CARD (name) VALUES (%s)"
    val = ("Michelle")
    cursor.execute(sql, val)