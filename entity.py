# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 15:28:57 2019

@author: Shaheer Akram
"""

import pandas as pd 
import re 

import nltk
import en_core_web_sm


def cleaner(message): 
    corpus = []
    for text in message:
        review = re.sub('[^a-zA-Z]', ' ', text)
        review = review.lower()
        review = review.split()
        review = ' '.join(review)
        corpus.append(review)
    return corpus

data = pd.read_excel('DataSetLeave_FinalMerge.xlsx',index_col = 0)
del data['SubClassess']
sent = data['Leave Data Description']

sen = '. '.join(sent)

sent = cleaner(sent)


import en_core_web_sm

en = en_core_web_sm.load()

sents = [en(s) for s in sent]
people = []
for sent in sents:    
    people.append([ee for ee in sent.ents if ee.label_ == 'PERSON'])
    
for en in people:
    print(en.text)



sen = en(sen)
people = [ee for ee in sen.ents if ee.label_ == 'PERSON']


doc_str = 'Electronically signed : Mr. Monis, M.D.; Jun 26 2010 11:10AM CST The patient was referred by Dr. Jacob Austin.  Electronically signed by Robert Clowson, M.D.; Janury 15 2015 11:13AM CST Electronically signed by Dr. John Douglas, M.D.; Jun 16 2017 11:13AM CST The patient was referred by Dr. Jayden Green Olivia. '

import en_core_web_md

en = en_core_web_md.load()

sen = en(doc_str)
people = [ee for ee in sen.ents if ee.label_ == 'PERSON']

for en in people:
    print(en.text)

for ent  in sen.ents:
    print(ent.text,ent.label_)

