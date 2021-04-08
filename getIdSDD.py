# TODO Fix get disk serial number
import xml.etree.ElementTree as ET

tree = ET.parse('disk.xml')
disk_xml = tree.getroot()

variableDesc = False
variableSerial =""

for child in disk_xml:
    for s in child:
        print(s.tag, s.text)
        if (s.tag == "description") and (s.text == "ATA Disk"):
            variableDesc = True
        if  (variableDesc == True) and (s.tag == "serial"):
            variableSerial = s.text
                print(variableSerial)

# class Hhd_Sdd:
#   def __init__(self, id_hhd_ssd, model_hhd_sdd):
#     self.id_hhd_ssd = id_hhd_ssd
#     self.model_hhd_sdd = model_hhd_sdd