import xmlrpclib
from env import *


common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
print(common.version())

def test(ee):
    print(ee)

def push_one_variantes(name_of_the_attribute, product_template_id, values, product_id):

    id_attribute = models.execute_kw(db, uid, password,
    'product.attribute', 'search',
    [[['name', '=', name_of_the_attribute ]]])
    print(' my id attribute', id_attribute)

    # code qui  genere un attribut de variantes au produit 1557
    create_attribute = models.execute_kw(db, uid, password, 'product.attribute.line', 'create', [{
    'product_tmpl_id': product_template_id , 'attribute_id': id_attribute[0]
    }])


    if type(values) == list:
        id_of_values = []
        for value in values:
             # code qui genere une valeur 538/ 539
            create_variable = models.execute_kw(db, uid, password, 'product.attribute.value', 'create', [{
            'name': value, 'attribute_id': id_attribute[0]
            }])
            id_of_values.append(create_variable)
    else:
        print(create_attribute,id_attribute[0], values, product_id )
        id_attribute_value = models.execute_kw(db, uid, password,
        'product.attribute.value', 'search',
        [[['name', '=', values ]]])
        print('my attribute value', id_attribute_value)
        # si la valeur existe deja
        if not id_attribute_value:
            print('elle existe pas')
            id_of_values = models.execute_kw(db, uid, password, 'product.attribute.value', 'create', [{
            'name': values, 'attribute_id': str(id_attribute[0])
            }])
            print(id_of_values)
            # code qui update value_ids 1561 ca marche!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            value_id = models.execute_kw(db, uid, password, 'product.attribute.line', 'write', [[create_attribute], {
            'value_ids': [(6,0,[id_of_values])]
            }])
            print("create value and raccordement to product", value_id)

        # sinon cree la
        else:

            # code qui update value_ids 1561 ca marche!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            # value_id = models.execute_kw(db, uid, password, 'product.attribute.line', 'create', [{
            # 'product_tmpl_id': product_template_id , 'attribute_id': id_attribute[0], 'value_ids': [(6,0,[id_attribute_value][0])]
            # }])
            print("la valeur existe deja")
            value_id = models.execute_kw(db, uid, password, 'product.attribute.line', 'write', [[create_attribute], {
            'value_ids': [(6,0,[id_attribute_value][0])]
            }])
            print("just racordement variantes product", value_id)



try:
    uid = common.authenticate(db, username, password, {})
    models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
    # check if have access
    print("check if i have accsse: ", models.execute_kw(db, uid, password,
    'product.product', 'check_access_rights',
    ['create'], {'raise_exception': False}))

    # check if i have the same serial number
    id_serial_number = models.execute_kw(db, uid, password,
    'stock.production.lot', 'search',
    [[['name', '=', 'violet 01' ]]])
    if id_serial_number:
        print('No update of database')
        print("read my serial number: ", models.execute_kw(db, uid, password,
        'stock.production.lot', 'read',
        [id_serial_number], {'fields': ['name', 'product_id']}))
    else:
        print("Test update dataBase")

        #create the product
        id_create_product = models.execute_kw(db, uid, password, 'product.product', 'create', [{
        'name': "yopop122", 'type': "product"
        }])
        
        # find id template
        yp = models.execute_kw(db, uid, password,
        'product.product', 'read',
        [id_create_product], {'fields': ['product_tmpl_id']})

        template_id = yp[0]['product_tmpl_id'][0]
        print(template_id, id_create_product)

        try:
            push_one_variantes('Processeur', template_id, 'lolololo', id_create_product)
        except:
            print("can't push variantes")

        # jj = models.execute_kw(db, uid, password,
        # 'product.template', 'search',
        # [[['id', '=', 'id_create_product' ]]])
        # print(models.execute_kw(db, uid, password,
        # 'product.template', 'read',
        # [jj], {'fields': ['display_name', 'is_product_variant', 'attribute_line_ids']}))

        # push_serial_number = models.execute_kw(db, uid, password, 'stock.production.lot', 'create', [{
        # 'name': "titi", 'product_id': "1575"
        # }])
        # print(push_serial_number)

        # code qui update my attribute value_ids 1561
        # models.execute_kw(db, uid, password, 'product.product', 'write', [[2],{
        # 'product_variant_ids': ['1582']
        # }])
        # print(models.execute_kw(db, uid, password, 'product.product', 'product_variant_ids_get', [[2]]))

        # id = models.execute_kw(db, uid, password, 'res.partner', 'create', [{
        # 'name': "tata", 'city': "Lyon", 'child_ids': ['6', '7']
        # }])
        # print(id)
        # 24734
        # models.execute_kw(db, uid, password, 'res.partner', 'write', [[24734], {
        # 'name': "diner"
        # }])
        # get record name after having changed it
        # print(models.execute_kw(db, uid, password, 'res.partner', 'name_get', [[24734]]))

        # create_product = models.execute_kw(db, uid, password, 'product.product', 'create', [{
        # 'name': "theproduct2", 'type': "product", 'attribute_line_ids': "1557", 
        # }])
        # print(create_product)


    

    # lds = models.execute_kw(db, uid, password,
    # 'product.attribute.line', 'search',
    # [[['id', '=', '2' ]]])
    # print("read my product.attribute.line: ", models.execute_kw(db, uid, password,
    # 'product.attribute.line', 'read',
    # [lds], {'fields': ['display_name', 'value_ids', 'product_tmpl_id', 'attribute_id']}))



    # ss = models.execute_kw(db, uid, password,
    # 'product.category', 'search',
    # [[['id', '=', '1' ]]])
    # print("read my product.category: ", models.execute_kw(db, uid, password,
    # 'product.category', 'read',
    # [ss], {'fields': ['display_name']}))


    #find id user
    # tt = models.execute_kw(db, uid, password,
    # 'res.users', 'search',
    # [[['email', '=', 'lisa.thazar@apside-groupe.com' ]]])
    # print("read my res.users: ", models.execute_kw(db, uid, password,
    # 'res.users', 'read',
    # [tt], {'fields': ['display_name']}))

    # create_variable = models.execute_kw(db, uid, password, 'product.attribute.value', 'create', [{
    # 'name': "zebi", 'attribute_id': "1"
    # }])
    # print(create_variable)



    # # check Id of variantes

    # id_processor_attributes = models.execute_kw(db, uid, password,
    # 'product.attribute', 'search',
    # [[['name', '=', 'Processeur' ]]])

    # id_graphic_card_attributes = models.execute_kw(db, uid, password,
    # 'product.attribute', 'search',
    # [[['name', '=', 'Carte Graphique' ]]])

    # id_fournisseur_attributes = models.execute_kw(db, uid, password,
    # 'product.attribute', 'search',
    # [[['name', '=', 'Fournisseur' ]]])

    # ids = models.execute_kw(db, uid, password,
    # 'product.product', 'search',
    # [[['name', '=', 'theproduct5' ]]])
    # print("read my product: ", models.execute_kw(db, uid, password,
    # 'product.product', 'read', [ids], {'fields': ['name', 'attribute_line_ids', 'product_variant_ids']}))
    # #[ids], {'fields': ['default_code', 'display_name', 'description', 'list_price', 'attribute_line_ids', 'categ_id', 'product_variant_ids', 'tracking', 'type', 'uom_id', 'uom_po_id' ]}))

    # kk = models.execute_kw(db, uid, password,
    # 'product.template', 'search',
    # [[['name', '=', 'theproduct2' ]]])
    # print("read my product template: ", models.execute_kw(db, uid, password,
    # 'product.template', 'read', [kk], {'fields': ['name', 'display_name', 'product_variant_ids', 'product_variant_id','attribute_line_ids']}))

    # ll = models.execute_kw(db, uid, password,
    # 'product.attribute.value', 'search',
    # [[['id', '=', '539' ]]])
    # print("read my product.attribute.value: ", models.execute_kw(db, uid, password,
    # 'product.attribute.value', 'read',
    # [ll], {'fields': ['display_name', 'name', 'product_ids', 'attribute_id']}))

    # xx = models.execute_kw(db, uid, password,
    # 'product.attribute', 'search',
    # [[['id', '=', '2' ]]])
    # print("read my product.attribute: ", models.execute_kw(db, uid, password,
    # 'product.attribute', 'read',
    # [xx], {'fields': ['display_name', 'name', 'attribute_line_ids', 'value_ids']}))

except:
    print("not works")


    