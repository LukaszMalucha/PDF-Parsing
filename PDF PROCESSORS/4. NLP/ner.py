# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 14:50:02 2020

@author: LukaszMalucha
"""

import spacy


# Preload library
nlp = spacy.load("en_core_web_sm")


doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")

print(doc.text)

print(doc[4])
print(doc[4].pos_)
print(doc[4].tag_)
print(doc[4].pos)
print(doc[4].tag)
  
for token in doc:
    print(f'{token.text:{10}} {token.pos_:{8}} {token.tag_:{6}} {spacy.explain(token.tag_)}')
    

doc = nlp(u'I read books on NLP.')
r = doc[1]

print(f'{r.text:{10}} {r.pos_:{8}} {r.tag_:{6}} {spacy.explain(r.tag_)}')



doc = nlp(u'I read a book on NLP.')
r = doc[1]

print(f'{r.text:{10}} {r.pos_:{8}} {r.tag_:{6}} {spacy.explain(r.tag_)}')



doc = nlp(u"The quick brown fox jumped over the lazy dog's back.")

POS_counts = doc.count_by(spacy.attrs.POS)

POS_counts

doc.vocab[83].text


for k,v in sorted(POS_counts.items()):
    print(f"{k}. {doc.vocab[k].text:{5}} {v}")


TAG_counts = doc.count_by(spacy.attrs.TAG)

for k,v in sorted(TAG_counts.items()):
    print(f"{k}. {doc.vocab[k].text:{5}} {v}")


########################################################################### NER




import spacy


# Preload library
nlp = spacy.load("en_core_web_sm")



def show_ents(doc):
    if doc.ents:
        for ent in doc.ents:
            print(ent.text + ' - ' + ent.label_ + ' - ' + str(spacy.explain(ent.label_)))
    else:
        print("No entities found")        


doc = nlp(u'Hi how are you?')


show_ents(doc)


doc = nlp(u'May I go to Washington, DC next May to see the Washington Monument?')

show_ents(doc)





doc = nlp(u'Can I please borrow 500 dollars from you to buy some Microsoft stock?')

for ent in doc.ents:
    print(ent.text, ent.start, ent.end, ent.start_char, ent.end_char, ent.label_)



doc = nlp(u'Tesla to build a U.K. factory for $6 million')

show_ents(doc)

###################
from spacy.tokens import Span

ORG = doc.vocab.strings[u"ORG"]

new_ent = Span(doc,0,1,label=ORG)

doc.ents = list(doc.ents) + [new_ent]

####################


doc = nlp(u'Our company plans to introduce a new vacuum cleaner. '
          u'If successful, the vacuum cleaner will be our first product.')

show_ents(doc)


from spacy.matcher import PhraseMatcher

matcher = PhraseMatcher(nlp.vocab)

phrase_list = ['vacuum cleaner', 'vacuum-cleaner']

phrase_patterns = [nlp(text) for text in phrase_list]

matcher.add('newproduct', None, *phrase_patterns)

found_matches = matcher(doc)

found_matches


from spacy.tokens import Span

PROD = doc.vocab.strings[u"PRODUCT"]


new_ents = [Span(doc, match[1], match[2], label=PROD) for match in found_matches]

# ADD NEW ENTITIES TO ORIGINAL
doc.ents = list(doc.ents) + new_ents

show_ents(doc)



doc = nlp(u'Originally priced at $29.50, the sweater was marked down to five dollars.')


show_ents(doc)


[ent for ent in doc.ents if ent.label_ == "MONEY"]




################################################################## SEGMENTATION

import spacy


# Preload library
nlp = spacy.load("en_core_web_sm")



doc = nlp(u'This is the first sentence. This is another sentence. This is the last sentence.')

# GENERATOR
for sent in doc.sents:
    print(sent)

list(doc.sents)[0]



######################################################### ADD SEGMENTATION RULE

def set_custom_boundries(doc):
    for token in doc[:-1]:
        if token.text == ";":
            doc[token.i + 1].is_sent_start = True
    return doc
    

nlp.add_pipe(set_custom_boundries, before='parser')

nlp.pipe_names

doc4 = nlp(u'"Management is doing things right; leadership is doing the right things." -Peter Drucker')

for sent in doc4.sents:
    print(sent)




###################################################### CHANGE SEGMENTATION RULE

nlp = spacy.load("en_core_web_sm")

mystring = u"This is a sentence. This is another.\n\nThis is a \nthird sentence."

doc = nlp(mystring)

for sentence in doc.sents:
    print(sentence)


from spacy.pipeline import SentenceSegmenter

def split_on_newlines(doc):
    start = 0
    seen_newline = False
    
    for word in doc:
        if seen_newline:
            yield doc[start:word.i]
            start = word.i
            seen_newline = False
        elif word.text.startswith('\n'):
            seen_newline = True
            
    yield doc[start:]
    

sbd = SentenceSegmenter(nlp.vocab, strategy=split_on_newlines)

nlp.add_pipe(sbd)

doc = nlp(mystring)

for sentence in doc.sents:
    print(sentence)
    






















