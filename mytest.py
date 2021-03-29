import xmlrpclib
from envtest import *

common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())

def push_one_variantes(name_of_the_attribute, product_template_id, values, product_id):
    id_attribute = models.execute_kw(db, uid, password,
    'product.attribute', 'search',
    [[['name', '=', name_of_the_attribute ]]])

    if not id_attribute:
        id_attribute_created = models.execute_kw(db, uid, password, 'product.attribute', 'create', [{
        'name': name_of_the_attribute
        }])
        id_attribute.append(id_attribute_created)


    print(' my id attribute', id_attribute)

    # code qui  genere un attribut de variantes au produit 1557
    create_attribute_line = models.execute_kw(db, uid, password, 'product.attribute.line', 'create', [{
    'product_tmpl_id': product_template_id , 'attribute_id': id_attribute[0]
    }])
    print("i have create my attribute line",create_attribute_line)

    id_of_values = []
    if type(values) == list:
        print('isLIST')
        for value in values:
             # code qui genere une valeur 538/ 539
        
            id_of_values.append(create_value_of_variable(value, str(id_attribute[0])))   
        #     create_variable = models.execute_kw(db, uid, password, 'product.attribute.value', 'create', [{
        #     'name': value, 'attribute_id': id_attribute[0]
        #     }])
        #     id_of_values.append(create_variable)
        # print("my id values", id_of_values)
    else:
        id_of_values.append(create_value_of_variable(values, str(id_attribute[0])))
    print("id of values:", id_of_values, create_attribute_line)
    value_id = models.execute_kw(db, uid, password, 'product.attribute.line', 'write', [[create_attribute_line], {
    'value_ids': [(6,0,id_of_values)]
    }])
    print("just racordement variantes product", value_id)

def create_value_of_variable(value, id_of_attribute):
    print(value, id_of_attribute)
    id_attribute_value_array = models.execute_kw(db, uid, password,
    'product.attribute.value', 'search',
    [['&',['name', '=', value ], [ 'attribute_id.id', '=', id_of_attribute]]])
    print(" my ids attribute values", id_attribute_value_array)
    # si la valeur existe deja
    if not id_attribute_value_array:
        print('La valeur attribuee n existe pas')
        id_attribute_value = models.execute_kw(db, uid, password, 'product.attribute.value', 'create', [{
        'name': value, 'attribute_id': id_of_attribute
        }])
        id_attribute_value_array.append(id_attribute_value)
        # code qui update value_ids 1561 ca marche!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # value_id = models.execute_kw(db, uid, password, 'product.attribute.line', 'write', [[create_attribute], {
        # 'value_ids': [(6,0,[id_of_values])]
        # }])
        # print("create value and raccordement to product", value_id)

    # sinon cree la
    else:
        print("la valeur existe deja", )
    print('my attribute value array', id_attribute_value_array)
        
    return id_attribute_value_array[0]


try:
    uid = common.authenticate(db, username, password, {})
    models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
    # check if have access
    # stock.quant without access
    try:

        print("check if i can do it: ", models.execute_kw(db, uid, password,
        'product.attribute.value', 'check_access_rights',
        ['create'], {'raise_exception': False}))

        name_product= models.execute_kw(db, uid, password,
        'product.product', 'search',
        [[['name', '=', 'beyonce' ]]])
        print(' name product', name_product)

        yp = models.execute_kw(db, uid, password,
        'product.product', 'read',
        [name_product], {'fields': ['product_tmpl_id']})

        template_id = yp[0]['product_tmpl_id'][0]

        try:
            push_one_variantes(u'Taille \xe9cran', template_id, float(15.5), name_product[0])
        except xmlrpclib.Error as err:
            print("can't push variantes Taille d ecran", err)


        # id_attribute = models.execute_kw(db, uid, password,
        # 'product.attribute.line', 'search',
        # [[([ 'attribute_id.id', '=', "9"])]])
        # print(id_attribute)


        # value_id = models.execute_kw(db, uid, password, 'product.attribute.line', 'write', [[1710], {
        # 'value_ids': [(6,0,[559])]
        # }])
    except xmlrpclib.Error as err:
        print('my error', err)


    print("read my stock productin: ", models.execute_kw(db, uid, password,
    'product.product', 'read',
    [491], {'fields': [ 'name', 'product_id', 'product_qty', 'product_tmpl_id']}))



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