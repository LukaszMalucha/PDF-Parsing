# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 12:52:59 2020

@author: LukaszMalucha
"""

from datetime import datetime

person = "Lukasz"


print(f"my name is {person}")

d = {"a":123, "b":456}


print(f"Number is {d['a']}")




library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]


for author, topic, pages in library:
    print(f"{author:{10}} {topic:{30}} {pages:->{10}}")
    
    
    
    
today = datetime(year=2019,month=2,day=28)    
    
    
    
print(f"{today:%B %d %Y}")    
    
    