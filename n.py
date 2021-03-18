import xmlrpclib
from env import *


common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())

def push_one_variantes(name_of_the_attribute, product_template_id, values, product_id):
    id_attribute = models.execute_kw(db, uid, password,
    'product.attribute', 'search',
    [[['name', '=', name_of_the_attribute ]]])
    print(' my id attribute', id_attribute)

    # code qui  genere un attribut de variantes au produit 1557
    create_attribute = models.execute_kw(db, uid, password, 'product.attribute.line', 'create', [{
    'product_tmpl_id': product_template_id , 'attribute_id': id_attribute[0]
    }])
    print(create_attribute, values)


    if type(values) == list:
        print('isLIST')
        id_of_values = []
        for value in values:
             # code qui genere une valeur 538/ 539
        
            id_of_values.append(create_value_of_variable(value, str(id_attribute[0])))   
        #     create_variable = models.execute_kw(db, uid, password, 'product.attribute.value', 'create', [{
        #     'name': value, 'attribute_id': id_attribute[0]
        #     }])
        #     id_of_values.append(create_variable)
        # print("my id values", id_of_values)
    else:
        create_value_of_variable(values, str(id_attribute[0]))
    print("idof values:", id_of_values)
    value_id = models.execute_kw(db, uid, password, 'product.attribute.line', 'write', [[create_attribute], {
    'value_ids': [(6,0,id_of_values)]
    }])
    print("just racordement variantes product", value_id)

    
def create_value_of_variable(value, id_attribute):
    id_attribute_value = models.execute_kw(db, uid, password,
    'product.attribute.value', 'search',
    [[['name', '=', value ]]])
    print('my attribute value', id_attribute_value)
    # si la valeur existe deja
    if not id_attribute_value:
        print('La valeur attribuee n existe pas')
        id_of_values = models.execute_kw(db, uid, password, 'product.attribute.value', 'create', [{
        'name': value, 'attribute_id': str(id_attribute[0])
        }])
        # code qui update value_ids 1561 ca marche!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # value_id = models.execute_kw(db, uid, password, 'product.attribute.line', 'write', [[create_attribute], {
        # 'value_ids': [(6,0,[id_of_values])]
        # }])
        # print("create value and raccordement to product", value_id)

    # sinon cree la
    else:
        print("la valeur existe deja")
        
    return id_attribute_value[0]

def create_serial_number():
    stock = models.execute_kw(db, uid, password,
    'stock.production.lot', 'search',
    [[['name', '=', 'serialNUMBER' ]]])
    if not stock:
        # cree numero de lot mais ne le lie pas a la product
        push_number_serie = models.execute_kw(db, uid, password, 'stock.production.lot', 'create', [{
        'name': "kekekeke", 'product_id': id_serial_number[0], 'product_qty':"1.0"
        }])
        print("kekekeke", push_number_serie)
        update_quantity_stock(push_number_serie)
    else:
        print('i have already a serial number')

def update_quantity_stock(push_number_serie):
    push_quantity = models.execute_kw(db, uid, password, 'stock.change.product.qty', 'create', [{
    'new_quantity': float(1.0), 'product_id': id_serial_number[0], 'lot_id': push_number_serie, 'location_id': "12"
    }])
    print('myquantity', push_quantity)
    # ca marcheee!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    models.execute_kw(db, uid, password, 'stock.change.product.qty', 'change_product_qty', [push_quantity])





try:
    uid = common.authenticate(db, username, password, {})
    models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
    # check if have access
    print("check if i have accsse   : ", models.execute_kw(db, uid, password,
    'product.product', 'check_access_rights',
    ['create'], {'raise_exception': False}))

    # check if i have the same name of product
    id_serial_number = models.execute_kw(db, uid, password,
    'product.product', 'search',
    [[['name', '=', 'dada' ]]])
    print(id_serial_number)
    if id_serial_number:
        print('No update of database')
        print("read my serial number: ", models.execute_kw(db, uid, password,
        'product.product', 'read',
        [id_serial_number[0]], {'fields': ['name', 'product_id']}))
        

    else:
        print("Test update dataBase")

        #create the product
        id_create_product = models.execute_kw(db, uid, password, 'product.product', 'create', [{
        'name': "AAA5", 'type': "product"
        }])
        
        # find id template
        yp = models.execute_kw(db, uid, password,
        'product.product', 'read',
        [id_create_product], {'fields': ['product_tmpl_id']})

        template_id = yp[0]['product_tmpl_id'][0]
        print(template_id, id_create_product)

        try:
            push_one_variantes('Processeur', template_id, ['lolololo', 'dede'], id_create_product)
        except:
            print("can't push variantes")

except:
    print("not works")


    