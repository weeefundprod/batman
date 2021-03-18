import xmlrpclib
from env import *

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())

try:
    uid = common.authenticate(db, username, password, {})
    models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
    # check if have access
    # stock.quant without access

    print("read my stock productin: ", models.execute_kw(db, uid, password,
    'product.product', 'read',
    [491], {'fields': [ 'name', 'product_id', 'product_qty', 'product_tmpl_id']}))

    print("check if i can do it: ", models.execute_kw(db, uid, password,
    'stock.production.lot', 'check_access_rights',
    ['create'], {'raise_exception': False}))

    # check if i have the same serial number
    id_serial_number = models.execute_kw(db, uid, password,
    'product.product', 'search',
    [[['name', '=', 'yopop1223' ]]])
    print(id_serial_number)

    stock = models.execute_kw(db, uid, password,
    'stock.location', 'search',
    [[['name', '=', 'WF' ]]])
    print('stock', stock)

    print("read my stock productin: ", models.execute_kw(db, uid, password,
    'stock.production.lot', 'read',
    [491], {'fields': [ 'name', 'product_id', 'product_qty', 'product_tmpl_id']}))
    print("read my stock productin: ", models.execute_kw(db, uid, password,
    'stock.production.lot', 'read',
    [497], {'fields': [ 'name', 'product_id', 'product_qty','product_tmpl_id']}))

    # 910
    id_stock = models.execute_kw(db, uid, password,
    'stock.change.product.qty', 'search',
    [[['id', '=', '956' ]]])
    print("here", id_stock)
    print("read my stock change ", models.execute_kw(db, uid, password,
    'stock.change.product.qty', 'read',
    [951], {'fields': [ 'new_quantity', 'product_id', 'lot_id', 'product_tmpl_id']}))



    # value_id = models.execute_kw(db, uid, password, 'stock.production.lot', 'write', [[495], {
    # 'product_qty': '1.0'
    # }])
    # print("create value and raccordement to product", value_id)

    # cree numero de lot mais ne le lie pas a la product
    # push_serial_number = models.execute_kw(db, uid, password, 'stock.production.lot', 'create', [{
    # 'name': "kekekeke", 'product_id': id_serial_number[0], 'product_qty':"1.0"
    # }])
    # print("kekekeke", push_serial_number)

    push_quantity = models.execute_kw(db, uid, password, 'stock.change.product.qty', 'create', [{
    'new_quantity': float(3.0), 'product_id': id_serial_number[0], 'lot_id': "495", 'location_id': "12"
    }])
    print('myquantity', push_quantity)
    # ca marcheee!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    models.execute_kw(db, uid, password, 'stock.change.product.qty', 'change_product_qty', [push_quantity])
    print("read my stock lot: ", models.execute_kw(db, uid, password,
    'stock.change.product.qty', 'read',
    [push_quantity], {'fields': [ 'new_quantity', 'product_id', 'lot_id', 'product_tmpl_id', 'location_id']}))

    id_quant = models.execute_kw(db, uid, password,
    'stock.quant', 'search',
    [[['quantity', '=', '5' ]]])
    print(id_quant)
    print("read quane: ", models.execute_kw(db, uid, password,
    'stock.quant', 'read',
    [1633], {'fields': [ 'name', 'product_id', 'product_qty', 'product_tmpl_id', 'quantity', 'location_id']}))


    # not works

    # id_quan = models.execute_kw(db, uid, password,
    # 'stock.inventory.line', 'search',
    # [[['product_qty', '=', '10' ]]])
    # print("dddd", id_quan)
    # print("read quant: ", models.execute_kw(db, uid, password,
    # 'stock.inventory.line', 'read',
    # [1621], {'fields': [ 'name', 'product_id', 'product_qty', 'product_tmpl_id', 'product_qty']}))

    # push = models.execute_kw(db, uid, password, 'stock.inventory.line', 'write', [[1621], {
    # 'product_qty': '1.0'
    # }])
    # print('my push', push)






except xmlrpclib.Error as err:
        print(err)