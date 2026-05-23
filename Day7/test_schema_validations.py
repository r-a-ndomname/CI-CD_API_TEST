import json
from pathlib import Path

import requests
import xmlschema
from jsonschema import ValidationError, validate

DAY7_DIR = Path(__file__).resolve().parent

class TestSchemaValidation:
    def test_json_schema_validation(self):
        url = "https://mocktarget.apigee.net/json"
        res = requests.get(url)

        assert res.status_code == 200, f"Wrong status code: {res.status_code}"

        data = res.json()

       
        with open(DAY7_DIR / "Jsonschema.json", "r", encoding="utf-8") as f:
            schema = json.load(f)

        try:
            validate(instance=data, schema=schema)
            print("JSON Schema validation passed")
        except ValidationError as e:
            print("JSON Schema validation failed")
            assert False

    def test_xml_schema_validation(self):
        url = "https://mocktarget.apigee.net/xml"
        res = requests.get(url)
        assert res.status_code == 200 

        #Load XML Schema
        schema = xmlschema.XMLSchema(DAY7_DIR / "xmlschema.xsd")

        try:
            schema.validate(res.text)
            print("XML Schema validation passed")
        except ValidationError as e:
            print("XML Schema validation failed")
            assert False