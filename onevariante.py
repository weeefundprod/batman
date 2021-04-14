import xmlrpclib
from env import *



common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))

try:
    uid = common.authenticate(db, username, password, {})
    models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
    # check if have access
    # stock.quant without access
    try:
        id_products= models.execute_kw(db, uid, password,
        'product.product', 'search',
        [[['name', '=', 'Asus FX553V' ]]])
        print(' name product', id_products)


        yp = models.execute_kw(db, uid, password,
        'product.product', 'read',
        [id_products], {'fields': ['attribute_value_ids', 'attribute_line_ids']})
        id_attribute_value = models.execute_kw(db, uid, password,
        'product.attribute.line', 'read',
        [1337], {'fields': ['attribute_id', 'product_tmpl_id', 'value_ids']})
        print(id_attribute_value[0]["value_ids"])


        values_ids = yp[0]["attribute_value_ids"]
        print('values id', values_ids)
        attr_ids = yp[0]["attribute_line_ids"]
        print('att id', attr_ids)
        
        id_attr_value =  models.execute_kw(db, uid, password,
        'product.attribute.value', 'search',
        [['&',['name', '=', 'bobo'], [ 'product_ids', '=', 1742]]])
        print("si attribute value est la ne touche pas sinon cree une variante et update le stock", id_attr_value)



        # print("id attribute line", id_attribute_value[0]["value_ids"])
        # other_ids.append(586)

        # value_id = models.execute_kw(db, uid, password, 'product.attribute.line', 'write', [[1337], {
        # 'value_ids': [(6,0,other_ids)]
        # }])
        # print("Raccordement variantes/product", value_id)
        # value = models.execute_kw(db, uid, password, 'product.attribute.value', 'write', [[586], {
        # 'product_ids': [(6,0,[1317])]
        # }])
        # print("valueeeeeee", value)

    except xmlrpclib.Error as err:
        print(err)



except xmlrpclib.Error as err:
        print(err)