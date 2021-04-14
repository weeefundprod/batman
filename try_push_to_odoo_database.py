import xmlrpclib
from env import *
from get_value_of_variantes import *

try:
    common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))
except xmlrpclib.Error as err:
    print(err)

# my function
def push_one_variante(name_of_the_attribute, product_template_id, values, product_id):
    #get or not the id of the attribute
    id_attributes = models.execute_kw(db, uid, password,
    'product.attribute', 'search',
    [[['name', '=', name_of_the_attribute ]]])
    # generere le nom  de la variante
    if not id_attributes:
        id_attribute_created = models.execute_kw(db, uid, password, 'product.attribute', 'create', [{
        'name': name_of_the_attribute
        }])
        id_attributes.append(id_attribute_created)
    # cherche attribut line
    id_attribute_line = models.execute_kw(db, uid, password,
    'product.attribute.line', 'search',
    [['&',['product_tmpl_id.id', '=', product_template_id ], [ 'attribute_id.id', '=', id_attributes[0]]]])
    if not id_attribute_line:
        print("si pas attribute line  creer une attribute line et une value")
        id_attribute_line = create_attribute_line()
        generate_value_of_variantes(value, attribute_line)
        link_value_to_product(value, attribute_line)
    else:
        print('verifie attribute value est bien  attribuée au produit')
        id_of_values = []
        if type(values) == list:
            for value in values:
                id_attr_value =  models.execute_kw(db, uid, password,
                'product.attribute.value', 'search',
                [['&',['name', '=', value], [ 'attribute_id.id', '=', id_attribute_line],[ 'product_ids', '=', product_id]]])
                print("si attribute value est la ne touche pas sinon cree une variante et update le stock", id_attr_value)
                id_of_values.append(generate_value_of_variantes(value, str(id_attributes[0])))
        else:
            id_of_values.append(generate_value_of_variantes(values, str(id_attributes[0])))
        
        # attr_value =  models.execute_kw(db, uid, password,
        # 'product.attribute.value', 'read',
        # [586], {'fields': ['display_name', 'name', 'product_ids', 'attribute_id', 'value_ids']})
        # print(attr_value)
        if not id_attr_value:
            same_product_with_same_variantes_exists = False
            generate_value_of_variantes(value, id_attribute_line[0])
        else:
            print("value is already created don't touch it")

def link_value_to_product(id_value, attribute_line, product_id):
    print("id attribute line", id_attribute_value[0]["value_ids"])
    read_line = models.execute_kw(db, uid, password, 'product.attribute.line', 'read',         
    [attribute_line], {'fields': ['attribute_id', 'product_tmpl_id', 'value_ids']})
    ids_attribute_line= read_line[0]["value_ids"]

    ids_attribute_line.append(value)

    update_attribute_line = models.execute_kw(db, uid, password, 'product.attribute.line', 'write', [[attribute_line], {
    'value_ids': [(6,0,ids_attribute_line)]
    }])
    update_attribute_value = models.execute_kw(db, uid, password, 'product.attribute.value', 'write', [[id_value], {
    'product_ids': [(6,0,[product_id])]
    }])
    print("Raccordement variantes/product", update_attribute_value, update_attribute_line )



def create_attribute_line(product_template_id, id_attribute ):
    # code qui  genere un attribut line de variantes au produit
    return models.execute_kw(db, uid, password, 'product.attribute.line', 'create', [{
    'product_tmpl_id': product_template_id , 'attribute_id': id_attribute
    }])
    # print("Je genere une ligne attribut ",name_of_the_attribute, values, " dont l'id est ", create_attribute_line)


def generate_value_of_variantes(value, id_of_attribute):
    id_attribute_value_array = models.execute_kw(db, uid, password,
    'product.attribute.value', 'search',
    [['&',['name', '=', value ], [ 'attribute_id.id', '=', id_of_attribute]]])

    # si la valeur existe pas
    if not id_attribute_value_array:
        print('La valeur de la variante :', value,' attribuee n existe pas')
        id_attribute_value = models.execute_kw(db, uid, password, 'product.attribute.value', 'create', [{
        'name': value, 'attribute_id': id_of_attribute
        }])
        id_attribute_value_array.append(id_attribute_value)

    # sinon cree la
    else:
        print("La valeur", value," existe deja" )
    return id_attribute_value_array[0]

def push_serial_number(id_product):
    stock = models.execute_kw(db, uid, password,
    'stock.production.lot', 'search',
    [[['ref', '=', serial_number ]]])
    if not stock:
        # cree numero de lot mais ne le lie pas a la product
        push_number_serie = models.execute_kw(db, uid, password, 'stock.production.lot', 'create', [{
        'name': internal_number, 'ref': serial_number, 'product_id': id_product, 'product_qty':"1.0"
        }])
        update_quantity_stock(push_number_serie)
    else:
        print('Il y a un numero de serie deja similaire entree dans la bdd Odoo ')

def update_quantity_stock(push_number_serie):
    push_quantity = models.execute_kw(db, uid, password, 'stock.change.product.qty', 'create', [{
    'new_quantity': float(1.0), 'product_id': id_product, 'lot_id': push_number_serie, 'location_id': "12"
    }])
    models.execute_kw(db, uid, password, 'stock.change.product.qty', 'change_product_qty', [push_quantity])
	print("Un nouveau stock avec le produit ", product, "serial number", serial_number, "numero interne", internal_number, "dans la bdd Odoo")

def verify_variantes_are_the_same(id_name_product):
    id_attribute_line = models.execute_kw(db, uid, password,
    'product.attribute.value', 'search',
    [['&',['name', '=', value ], [ 'attribute_id.id', '=', id_of_attribute]]])





# beginning of the script
try:
    try:
        uid = common.authenticate(db, username, password, {})
    except xmlrpclib.Error as err:
        print("Authentification error",err)
    models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
    # check if have access
    # print("check if I have access to Odoo create product: ", models.execute_kw(db, uid, password,
    # 'product.product', 'check_access_rights',
    # ['create'], {'raise_exception': False}))

    # check if i have the same name of product
    # warning ne prends pas en compte si il y a les memes produits avec les mm noms
    id_same_name_products = models.execute_kw(db, uid, password,
    'product.product', 'search',
    [[['name', '=', product ]]])
    if id_same_name_products:
        print('Produit similaire dans la base de donnees Odoo')
        same_product_with_same_variantes_exists = True
        for id_product in id_same_name_products:
            product_to_read = models.execute_kw(db, uid, password,
            'product.product', 'read',
            [id_name_product], {'fields': ['product_tmpl_id', 'attribute_value_ids', 'attribute_line_ids']})

            print("My product: ", product_to_read)

            template_id = product_to_read[0]['product_tmpl_id'][0]
             # verify the variantes are the same
            try:
                push_one_variante('Processeur', template_id, processor, id_product)
            except:
                print("can't push variantes Processeur")
            
            if [same_product_with_same_variantes_exists == True]:
                print("just update le stock")
                push_serial_number(id_product)
            else:
                print("try other product")
        
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

        try:
            push_one_variante('Processeur', template_id, processor, id_product)
        except:
            print("can't push variantes Processeur")

        try:
            push_one_variante('Carte Graphique', template_id, graphic_card, id_product)
        except:
            print("can't push variantes Processeur")
        try:
            push_one_variante('RAM', template_id, ram, id_product)
        except:
            print("can't push variantes RAM")
        try:
            push_one_variante(u'Taille \xe9cran', template_id, screen, id_product)
        except:
            print("can't push variantes Taille d ecran")
        try:
            push_one_variante('Marque', template_id, vendor, id_product)
        except:
            print("can't push variantes Marque")
        try:
            push_one_variante('DVD', template_id, dvd, id_product)
        except:
            print("can't push variantes DVD")
        try:
            push_one_variante('BLUETOOTH', template_id, bluetooth, id_product)
        except:
            print("can't push variantes bluetooth")
        try:
            push_one_variante('HHDSSD', template_id, array_hhd_sdd, id_product)
        except:
            print("can't push variantes hddssd")
        # try:
        #     push_one_variante('In', template_id, internal_number, id_product)
        # except:
        #     print("can't push variantes numero de lot")
    push_serial_number(id_product)
        

except xmlrpclib.Error as err:
    print(err)