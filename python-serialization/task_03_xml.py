#!/usr/bin/python3
"""
this is a module for interpreting python3
"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    serialize a dictionary to xml and save inside filename
    """
    data = ET.parse(data.xml)
    data = data.getroot()

    for child in data:
        print(child.tag, child.attrib)
