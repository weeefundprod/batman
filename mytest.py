import xmlrpclib
from env import *

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())

try:
    uid = common.authenticate(db, username, password, {})
    models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
    # check if have access
    # stock.quant without access
    try:

        # id_attribute = models.execute_kw(db, uid, password,
        # 'product.attribute.line', 'search',
        # [[([ 'attribute_id.id', '=', "9"])]])
        # print(id_attribute)
        id_attribute = models.execute_kw(db, uid, password,
        'product.attribute.value', 'search',
        [['&',['name', '=', 'oui'] , [ 'attribute_id.id', '=', '39']]])
        print(id_attribute)

        print("read my stock productin: ", models.execute_kw(db, uid, password,
        'product.attribute.line', 'read',
        [260], {'fields': [ 'name', 'attribute_id', 'product_tmpl_id']}))


        # value_id = models.execute_kw(db, uid, password, 'product.attribute.line', 'write', [[1710], {
        # 'value_ids': [(6,0,[559])]
        # }])
    except xmlrpclib.Error as err:
        print('my error', err)


    print("read my stock productin: ", models.execute_kw(db, uid, password,
    'product.product', 'read',
    [491], {'fields': [ 'name', 'product_id', 'product_qty', 'product_tmpl_id']}))

    print("check if i can do it: ", models.execute_kw(db, uid, password,
    'stock.production.lot', 'check_access_rights',
    ['create'], {'raise_exception': False}))

    # check if i have the same serial number
    id_serial_number = models.execute_kw(db, uid, password,
    'product.attribute', 'search',
    [[['name', '=', 'DVD' ]]])
    print(id_serial_number)

    print("read my product.attribute.value: ", models.execute_kw(db, uid, password,
    'product.attribute', 'read',
    [id_serial_number], {'fields': ['display_name', 'name', 'product_ids', 'attribute_id']}))








except xmlrpclib.Error as err:
        print(err)