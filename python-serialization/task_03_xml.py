#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    serialize a dictionary to xml and save inside filename
    """
    root = ET.Element('data')
    tree.write(filename, encoding="utf-8", xml_declaration=True)