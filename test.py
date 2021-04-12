import xmlrpclib
from env import *

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())
uid = common.authenticate(db, username, password, {})
models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
    # check if have access
    # stock.quant without access
try:
    stock = models.execute_kw(db, uid, password,
    'stock.production.lot', 'search',
    [[['ref', '=', 'JCN0CX10U0381B' ]]])
    print(stock)
    # print("My actual id: ", models.execute_kw(db, uid, password,
    # 'stock.production.lot', 'read',
    # [stock[0]], {'fields': ['name', 'product_id']}))
    # push_number_serie = models.execute_kw(db, uid, password, 'stock.production.lot', 'create', [{
    # 'name': "sjsj", 'ref': 'JCN0CX10U031', 'product_id': 1318, 'product_qty':"1.0"
    # }])
    # print(push_number_serie)
    push_quantity = models.execute_kw(db, uid, password, 'stock.change.product.qty', 'create', [{
    'new_quantity': float(1.0), 'product_id': 1318, 'lot_id': 1102, 'location_id': "12"
    }])
    models.execute_kw(db, uid, password, 'stock.change.product.qty', 'change_product_qty', [push_quantity])
except xmlrpclib.Error as err:
    print(err)