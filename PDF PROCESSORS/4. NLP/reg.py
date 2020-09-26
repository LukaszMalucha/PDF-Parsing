# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 16:01:51 2020

@author: LukaszMalucha
"""

import re

text = "the phone number is 408-123-4567. Call us!"

"phone" in text


pattern = "phone"


my_match = re.search(pattern, text)

my_match.span()
my_match.end()


text_2 = "my phone is a new phone"

match = re.search(pattern, text_2)

match.span()



match_all = len(re.findall(pattern, text_2))


for match in re.finditer(pattern, text_2):
    print(match.span())
    
pattern = r"(\d{2,4})-(\d{2,5})-(\d{3,5})"

phone_number = re.findall(pattern, text)


re.search(r"man|woman", "This woman was here")



re.findall(r".at", "The cat in the hat sat splat")


re.findall(r"\d$", "This ends with a number 2")



phrase = "there are 3 numbers 34 inside 5 this sentence"


re.findall(r"[^\d]+", phrase)








































