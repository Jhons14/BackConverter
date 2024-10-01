from flask import Flask, request, jsonify
from src.converter import json_to_xml, xml_to_json
import json
from dicttoxml import dicttoxml
import xmltodict

app = Flask(__name__)

@app.route('/convert/xml-to-json', methods=['POST'])
def convert_xml_to_json():
    xml_data = request.data.decode('utf-8')  # Obtener XML del body de la petición
    try:
        json_result = xml_to_json(xml_data)  # Convertir XML a JSON
        return jsonify(json_result), 200  # Devolver el JSON convertido
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Manejo de errores

@app.route('/convert/json-to-xml', methods=['POST'])
def convert_json_to_xml():
    json_data = request.json  # Obtener JSON del body de la petición
    try:
        xml_result = json_to_xml(json.dumps(json_data))  # Convertir JSON a XML
        return xml_result, 200, {'Content-Type': 'application/xml'}  # Devolver el XML convertido
    except Exception as e:
        return jsonify({'error': str(e)}), 400  # Manejo de errores

if __name__ == "__main__":
    app.run(debug=True)
