import xmlrpclib
from env import *

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())

try:
    uid = common.authenticate(db, username, password, {})
    models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
    # check if have access
    print("check if i can do it: ", models.execute_kw(db, uid, password,
    'product.attribute.line', 'check_access_rights',
    ['create'], {'raise_exception': False}))

    lds = models.execute_kw(db, uid, password,
    'product.attribute', 'search',
    [[['name', '=', 'Carte Graphique' ]]])
    print("read my product.attribute: ", models.execute_kw(db, uid, password,
    'product.attribute', 'read',
    [lds], {'fields': ['display_name', 'value_ids', 'product_tmpl_id', 'attribute_id']}))

    create_attribute = models.execute_kw(db, uid, password, 'product.attribute.line', 'create', [{
    'product_tmpl_id': '722' , 'attribute_id': '2'
    }])
    print(create_attribute)

    create_variable = models.execute_kw(db, uid, password, 'product.attribute.value', 'create', [{
    'name': "DDDDD", 'attribute_id': '2'
    }])

    print(create_variable)

    c = models.execute_kw(db, uid, password, 'product.attribute.value', 'create', [{
    'name': "TTTT", 'attribute_id': '2'
    }])

    print(c)

    value_id = models.execute_kw(db, uid, password, 'product.attribute.line', 'write', [[create_attribute], {
    'value_ids': [(6,0,[c,create_variable])]
    }])




except:
    print("not works")