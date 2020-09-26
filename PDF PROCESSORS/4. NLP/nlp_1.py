# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 16:48:30 2020

@author: LukaszMalucha
"""

# pip install spacy
# python -m spacy download en

import spacy

# Preload library
nlp = spacy.load("en_core_web_sm")


######################################################################### BASIC
# Tokenize
doc = nlp(u"Tesla is looking at buying U.S. startup for $6 million")


# Part of Speech (POS)
for token in doc:
    print(token.text, token.pos_, token.dep_)


nlp.pipeline


doc2 = nlp(u"Tesla isn't looking into startups anymore.")


for token in doc2:
    print(token.text, token.pos_, token.dep_)
    
doc2[0].pos_
doc2[0].is_alpha

###################################################################### TOKENIZE

mystring = '"We\'re moving to L.A.!"'

print(mystring)

doc = nlp(mystring)

for token in doc:
    print(token.text)


doc2 = nlp(u"We're here to help! Send snail-mail, email support@oursite.com or visit us at http://www.oursite.com!")

for t in doc2:
    print(t)



doc3 = nlp(u'A 5km NYC cab ride costs $10.30')

for t in doc3:
    print(t)


doc4 = nlp(u"Let's visit St. Louis in the U.S. next year.")

for t in doc4:
    print(t)


doc4.vocab


doc8 = nlp(u'Apple to build a Hong Kong factory for $6 million')

for token in doc8:
    print(token.text, end=' | ')

print('\n----')

for ent in doc8.ents:
    print(ent.text+' - '+ent.label_+' - '+str(spacy.explain(ent.label_)))


doc9 = nlp(u"Autonomous cars shift insurance liability toward manufacturers.")

for chunk in doc9.noun_chunks:
    print(chunk.text)

# DISPLAYING
from spacy import displacy
 
doc = nlp(u'Apple is going to build a U.K. factory for $6 million.')
displacy.render(doc, style='dep', options={'distance': 110})
displacy.render(doc, style='ent', options={'distance': 110})



################################################################# LEMMATIZATION


doc1 = nlp(u"I am a runner running in a race because I love to run since I ran today")

for token in doc1:
    print(token.text, '\t', token.pos_, '\t', token.lemma, '\t', token.lemma_)


def show_lemmas(text):
    for token in text:
        print(f'{token.text:{12}} {token.pos_:{6}} {token.lemma:<{22}} {token.lemma_}')
        
        
        
doc2  = nlp(u"I saw ten mice today!")     

show_lemmas(doc2)  
        
        
#################################################################### STOP WORDS

print(nlp.Defaults.stop_words)

# ADD STOPWORD
nlp.Defaults.stop_words.add('btw')

nlp.vocab['btw'].is_stop = True

len(nlp.Defaults.stop_words)


# Remove
nlp.Defaults.stop_words.remove('btw')
nlp.vocab['btw'].is_stop = False
nlp.vocab['btw'].is_stop


######################################################### VOCABULARY & MATCHING



from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)

# appears as 'SolarPower', 'solar-power', 'Solar power'




pattern1 = [{'LOWER': 'solarpower'}] 
pattern2 = [{'LOWER': 'solar'}, {'IS_PUNCT':True}, {'LOWER':'power'}] 
pattern3 = [{'LOWER': 'solar'}, {'LOWER':'power'}] 



matcher.add('SolarPower', None, pattern1, pattern2, pattern3)


doc = nlp(u'The Solar Power industry continues to grow as demand \
for solarpower increases. Solar-power cars are gaining popularity.')



found_matches = matcher(doc)

print(found_matches)




for match_id, start, end in found_matches:
    string_id = nlp.vocab.strings[match_id]  # get string representation
    span = doc[start:end]                    # get the matched span
    print(match_id, string_id, start, end, span.text)


matcher.remove('SolarPower')


pattern1 = [{'LOWER': 'solarpower'}]

# OP FOR ANY AMOUNT OF PUNCTUATION
pattern2 = [{'LOWER': 'solar'}, {'IS_PUNCT': True, 'OP':'*'}, {'LOWER': 'power'}]


matcher.add('SolarPower', None, pattern1, pattern2)



found_matches = matcher(doc)
print(found_matches)


























