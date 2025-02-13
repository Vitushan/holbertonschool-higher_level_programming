#!/usr/bin/python3
"""
explore serialization and deserialization using XML as an alternative format to JSON
"""


import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    serialize a dictionary in xml file and save it.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        item = ET.SubElement(root, key)
        item.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    deserialize from xml in python dictionary
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    data_dict = {}
    for child in root:
        data_dict[child.tag] = child.text
    return data_dict
