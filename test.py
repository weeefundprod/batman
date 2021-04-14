import xmlrpclib
from env import *

# my function
def push_one_variante(name_of_the_attribute, product_template_id, values, product_id):
    #get or not the id of the attribute
    id_attributes = models.execute_kw(db, uid, password,
    'product.attribute', 'search',
    [[['name', '=', name_of_the_attribute ]]])

    if not id_attributes:
        id_attribute_created = models.execute_kw(db, uid, password, 'product.attribute', 'create', [{
        'name': name_of_the_attribute
        }])
        id_attributes.append(id_attribute_created)

    # code qui  genere un attribut line de variantes au produit
    create_attribute_line = models.execute_kw(db, uid, password, 'product.attribute.line', 'create', [{
    'product_tmpl_id': product_template_id , 'attribute_id': id_attributes[0]
    }])
    print("Je genere une ligne attribut",name_of_the_attribute, values)

    id_of_values = []
    if type(values) == list:
        for value in values:
            id_of_values.append(get_id_of_value_of_variantes(value, str(id_attributes[0])))
    else:
        id_of_values.append(get_id_of_value_of_variantes(values, str(id_attributes[0])))
    print("Id des valeurs :", id_of_values, "Id des lignes attributions: ", create_attribute_line)
    value_id = models.execute_kw(db, uid, password, 'product.attribute.line', 'write', [[create_attribute_line], {
    'value_ids': [(6,0,id_of_values)]
    }])
    print("Raccordement variantes/product", value_id)
    value = models.execute_kw(db, uid, password, 'product.attribute.value', 'write', [[id_of_values[0]], {
    'product_ids': [(6,0,[product_id])]
    }])
    print("valueeeeeee", value)

def get_id_of_value_of_variantes(value, id_of_attribute):
    id_attribute_value_array = models.execute_kw(db, uid, password,
    'product.attribute.value', 'search',
    [['&',['name', '=', value ], [ 'attribute_id.id', '=', id_of_attribute]]])

    # si la valeur existe pas
    if not id_attribute_value_array:
        print('La valeur de la variante :', value,' attribuee n existe pas')
        id_attribute_value = models.execute_kw(db, uid, password, 'product.attribute.value', 'create', [{
        'name': value, 'attribute_id': id_of_attribute,
        }])
        id_attribute_value_array.append(id_attribute_value)

    # sinon cree la
    else:
        print("La valeur", value," existe deja" )
    return id_attribute_value_array[0]



common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))



try:
    uid = common.authenticate(db, username, password, {})
    models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
    # check if have access
    # stock.quant without access
    try:

        id_product= 1317
        id_products= models.execute_kw(db, uid, password,
        'product.product', 'search',
        [[['name', '=', 'Asus FX553V' ]]])
        print(' name product', id_products)


        yp = models.execute_kw(db, uid, password,
        'product.product', 'read',
        [id_product], {'fields': ['product_tmpl_id', 'attribute_value_ids', 'attribute_line_ids']})

        print("My product: ", yp)

        template_id = yp[0]['product_tmpl_id'][0]

        # try:
        #     push_one_variantes(u'Taille \xe9cran', template_id, float(15.5), name_product[0])
        # except xmlrpclib.Error as err:
        #     print("can't push variantes Taille d ecran", err)


        id_attribute = models.execute_kw(db, uid, password,
        'product.attribute.line', 'read',
        [1337], {'fields': ['product_tmpl_id', 'attribute_id', 'value_ids']})
        print("My attribute Line: ", id_attribute)


        # value_id = models.execute_kw(db, uid, password, 'product.attribute.line', 'write', [[1710], {
        # 'value_ids': [(6,0,[559])]
        # }])
    except xmlrpclib.Error as err:
        print('my error', err)
    same_product_with_same_variantes_exists = True
    # boucle dans les produits
    #for all in variantes:
        # boucle sur toutes les variantes
        # si l'attribute line n'est pas relie au produit
    id_attribute_line = models.execute_kw(db, uid, password,
    'product.attribute.line', 'search',
    [['&',['product_tmpl_id.id', '=', 459 ], [ 'attribute_id.id', '=', 1]]])
    print(" search id attribute line on the product asus", id_attribute_line)
    if not id_attribute_line:
        print("not attribute line  creer une attribute line et une value")
        create_attribute_line()
        link_value_to_product(value, id_attribute_line[0])
    else:
        print('verifie si il y a une attribute value')
        id_attr_value =  models.execute_kw(db, uid, password,
        'product.attribute.value', 'search',
        [['&',['name', '=', 'bobo'], [ 'attribute_id.id', '=', 1],[ 'product_ids', '=', 1317]]])
        print("si attribute value est la ne touche pas sinon cree une variante et update le stock", id_attr_value)
        # attr_value =  models.execute_kw(db, uid, password,
        # 'product.attribute.value', 'read',
        # [586], {'fields': ['display_name', 'name', 'product_ids', 'attribute_id', 'value_ids']})
        # print(attr_value)
        if not id_attr_value:
            same_product_with_same_variantes_exists = False
            get_id_of_value_of_variantes(value, id_attribute_line[0])
        else:
            print("value is already created don't touch it")
    if [same_product_with_same_variantes_exists == True]:
        print("just update le stock")
    else:
        print("try other product")
            
        


    # id_attribute_value = models.execute_kw(db, uid, password,
    # 'product.attribute.value', 'search',
    # [['&',['name', '=', 'TEST' ], [ 'product_ids', '=', name_product]]])
    # print("id attribute", id_attribute_value)
    # if not id_attribute_value:
    #     push_one_variante('Processeur', 459, "bobo", 1317)



except xmlrpclib.Error as err:
        print(err)