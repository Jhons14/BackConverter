import json
from dicttoxml import dicttoxml
import xmltodict

def json_to_xml(json_data):
    data_dict = json.loads(json_data)
    xml_data = dicttoxml(data_dict, custom_root='root', attr_type=False)
    return xml_data.decode()

def xml_to_json(xml_data):
    data_dict = xmltodict.parse(xml_data)
    json_data = json.dumps(data_dict, indent=4)
    return json_data