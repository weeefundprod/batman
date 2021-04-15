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
    id_attr_value =  models.execute_kw(db, uid, password,
    'product.attribute.value', 'search',
    [['&',['name', '=', 'graohic'], [ 'attribute_id.id', '=', 2],[ 'product_ids', '=', id_product]]])
    id_attribute_value = models.execute_kw(db, uid, password,
    'product.attribute.value', 'read',
    id_attr_value, {'fields': ['attribute_id', 'product_tmpl_id', 'name', "product_ids"]})
    print("attribute vaalue", id_attribute_value)
    print(id_attr_value)



except xmlrpclib.Error as err:
    print(err)

