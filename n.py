import xmlrpclib
from env import *
from p import *


common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())

def push_one_variantes(name_of_the_attribute, product_template_id, values, product_id):
    id_attribute = models.execute_kw(db, uid, password,
    'product.attribute', 'search',
    [[['name', '=', name_of_the_attribute ]]])

    if not id_attribute:
        id_attribute[0] = models.execute_kw(db, uid, password, 'product.attribute', 'create', [{
        'name': name_of_the_attribute
        }])

    print(' my id attribute', id_attribute)

    # code qui  genere un attribut de variantes au produit 1557
    create_attribute_line = models.execute_kw(db, uid, password, 'product.attribute.line', 'create', [{
    'product_tmpl_id': product_template_id , 'attribute_id': id_attribute[0]
    }])
    print(create_attribute_line, values)


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
    value_id = models.execute_kw(db, uid, password, 'product.attribute.line', 'write', [[create_attribute_line], {
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

def create_serial_number(id_product):
    stock = models.execute_kw(db, uid, password,
    'stock.production.lot', 'search',
    [[['name', '=', 'serialNUMBER' ]]])
    if not stock:
        # cree numero de lot mais ne le lie pas a la product
        push_number_serie = models.execute_kw(db, uid, password, 'stock.production.lot', 'create', [{
        'name': serial, 'product_id': id_product, 'product_qty':"1.0"
        }])
        print("kekekeke", push_number_serie)
        update_quantity_stock(push_number_serie)
    else:
        print('i have already a serial number')

def update_quantity_stock(push_number_serie):
    push_quantity = models.execute_kw(db, uid, password, 'stock.change.product.qty', 'create', [{
    'new_quantity': float(1.0), 'product_id': id_product, 'lot_id': push_number_serie, 'location_id': "12"
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
    name_product = models.execute_kw(db, uid, password,
    'product.product', 'search',
    [[['name', '=', product ]]])
    print(' name product', name_product)
    if name_product:
        print('I have the name  i got to see the serial number')
        print("read my serial number: ", models.execute_kw(db, uid, password,
        'product.product', 'read',
        [name_product[0]], {'fields': ['name', 'product_id']}))
        id_product = name_product[0]
        

    else:
        print("I create a new product")

        #create the product
        id_product = models.execute_kw(db, uid, password, 'product.product', 'create', [{
        'name': product, 'type': "product"
        }])
        
        # find id template
        yp = models.execute_kw(db, uid, password,
        'product.product', 'read',
        [id_product], {'fields': ['product_tmpl_id']})

        template_id = yp[0]['product_tmpl_id'][0]
        print(template_id, id_product)

        try:
            push_one_variantes('Processeur', template_id, processor, id_product)
        except:
            print("can't push variantes Processeur")

        try:
            push_one_variantes('Carte Graphique', template_id, graphic_card, id_product)
        except:
            print("can't push variantes Processeur")
        try:
            push_one_variantes('RAM', template_id, processor, id_product)
        except:
            print("can't push variantes RAM")
        try:
            push_one_variantes(u'Taille \xe9cran', template_id, screens, id_product)
        except:
            print("can't push variantes Taille d ecran")
        try:
            push_one_variantes('Marque', template_id, vendor, id_product)
        except:
            print("can't push variantes Marque")
        try:
            push_one_variantes('DVD', template_id, vendor, id_product)
        except:
            print("can't push variantes DVD")
        try:
            push_one_variantes('BLUETOOTH', template_id, bluetooth, id_product)
        except:
            print("can't push variantes bluetooth")
        try:
            push_one_variantes('HHDSSD', template_id, hhdssd, id_product)
        except:
            print("can't push variantes hddssd")
    create_serial_number(id_product)
        

except xmlrpclib.Error as err:
    print(err)