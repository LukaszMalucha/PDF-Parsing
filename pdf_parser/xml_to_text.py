# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 13:42:52 2020

@author: LukaszMalucha
"""


from xml.etree import cElementTree as ET

tree = ET.parse("2020-02-02-13-54-25-image.xml")

root = tree.getroot()

print(root)