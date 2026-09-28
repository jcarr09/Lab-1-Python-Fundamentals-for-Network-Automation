import json
import yaml
import xml.etree.ElementTree as ET
import csv
import logging

def parse_json(filename):
    try:
        with open(filename, "r") as file:
            jsondata = json.load(file)
        logging.info("PARSE_JSON_SUCCESS")
        return jsondata
    except (FileNotFoundError, json.JSONDecodeError):
        logging.error("PARSE_JSON_ERROR")
        return []
    
def parse_yaml(filename):
    try:
        with open(filename, "r") as file:
            yamldata = yaml.safe_load(file)
        logging.info("PARSE_YAML_SUCCESS")
        return yamldata.get("interfaces", [])
    except (FileNotFoundError, yaml.YAMLError):
        logging.error("PARSE_YAML_ERROR")
        return []

def parse_xml(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        xmldata = []
        for child in root.findall("vlan"):
            xmldata.append({
                "id": child.findtext("id"),
                "name": child.findtext("name"),
            })
        logging.info("PARSE_XML_SUCCESS")
        return xmldata
    except (FileNotFoundError, ET.ParseError):
        logging.error("PARSE_XML_ERROR")
        return []

def parse_csv(filename):
    try:
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            csvdata = list(reader)
        logging.info("PARSE_CSV_SUCCESS")
        return csvdata
    except FileNotFoundError:
        logging.error("PARSE_CSV_ERROR")
        return []