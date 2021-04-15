import xmlrpclib
from env import *
from dumb import *



common = xmlrpclib.ServerProxy('{}/xmlrpc/2/common'.format(url))


try:
    uid = common.authenticate(db, username, password, {})
    models = xmlrpclib.ServerProxy('{}/xmlrpc/2/object'.format(url))
    # check if have access
    # stock.quant without access
    try:
        id_products= models.execute_kw(db, uid, password,
        'product.product', 'search',
        [[['name', '=', 'mama' ]]])
        print(id_products)
        id_product= models.execute_kw(db, uid, password,
        'product.attribute.line', 'read',
        [1766], {'fields': ['value_ids', 'product_ids', 'attribute_line_ids', 'product_id', 'product_ids',"product_tmpl_id"]})
        print(id_product)
        id_tmpl= models.execute_kw(db, uid, password,
        'product.attribute.value', 'search',
        [[['name', '=', 'mm' ]]])
        print(id_tmpl)
        # id_product = models.execute_kw(db, uid, password, 'product.product', 'create', [{
        # 'name': "mama", 'type': "product"
        # }])

        what=models.execute_kw(db, uid, password, 'product.template', 'create_variant_ids', [777])
        print(what)



# class ProductTemplate(models.Model):

# _inherit = "product.template"

# def create_variant_ids(self):

# archived_product_variants_ids = self.env['product.product'].search([('product_tmpl_id','=',self.id),('active','=',False)])

# super(ProductTemplate, self).create_variant_ids()

# result = archived_product_variants_ids.write({'active':False})

        # yp = models.execute_kw(db, uid, password,
        # 'product.template', 'read',
        # [767], {'fields': ['name', 'attribute_line_ids',"product_variant_count", "value_ids",'product_variant_id', 'product_variant_ids']})
        # print("yolooooooooooo", yp)
        # id_attribute_line = models.execute_kw(db, uid, password,
        # 'product.attribute.line', 'read',
        # [1740], {'fields': ['attribute_id', 'product_tmpl_id', 'value_ids']})
        # print(id_attribute_line)
        # id_attribute_value = models.execute_kw(db, uid, password,
        # 'product.attribute.value', 'read',
        # [610], {'fields': ['attribute_id', 'product_tmpl_id', 'name', "product_ids"]})
        # print("attribute vaalue", id_attribute_value)

        # id_product = models.execute_kw(db, uid, password, 'product.product', 'create', [{
        # 'name': "requin", 'type': "product", "is_product_variant": True, "product_variant_id": [(6,0,[1793])]
        # }])

    # update_attribute_line = models.execute_kw(db, uid, password, 'product.attribute.line', 'write', [attribute_line, {
    # 'value_ids': [(6,0,ids_attribute_value)]
    # }])
    # print(update_attribute_line, "myy update")
    # update_attribute_value = models.execute_kw(db, uid, password, 'product.attribute.value', 'write', [id_value, {
    # 'product_ids': [(6,0,[product_id])]
    # }])




        # values_ids = yp[0]["attribute_value_ids"]
        # print('values id', values_ids)
        # attr_ids = yp[0]["attribute_line_ids"]
        # print('att id', attr_ids)
        
        # id_attr_value =  models.execute_kw(db, uid, password,
        # 'product.attribute.value', 'search',
        # [['&',['name', '=', 'bobo'], [ 'product_ids', '=', 1742]]])
        # print("si attribute value est la ne touche pas sinon cree une variante et update le stock", id_attr_value)



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