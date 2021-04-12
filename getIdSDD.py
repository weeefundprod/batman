import xml.etree.ElementTree as ET

tree = ET.parse('t.xml')
disk_xml = tree.getroot()

variableDesc = False
variableSerial =""
array_hhd_sdd = []
array_id_hhd_sdd = []

for child in disk_xml:
    for s in child:
        if (s.tag == "description") and (s.text == "ATA Disk"):
            variableDesc = True
        if  (variableDesc == True) and (s.tag == "serial"):
            variableSerial = s.text
            array_hhd_sdd.append(variableSerial)
        if  (variableDesc == True) and (s.tag == "product"):
            id_hhd_sdd = s.text
            array_id_hhd_sdd.append(id_hhd_sdd)
    variableDesc = False
print(array_hhd_sdd)
print(array_id_hhd_sdd)

# class Hhd_Sdd:
#   def __init__(self, id_hhd_ssd, model_hhd_sdd):
#     self.id_hhd_ssd = id_hhd_ssd
#     self.model_hhd_sdd = model_hhd_sdd