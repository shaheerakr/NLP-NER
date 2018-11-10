# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 00:14:36 2018

@author: Shaheer Akram
"""
!pip install nltk
import nltk
nltk.download()
from nltk.tokenize import word_tokenize
import pandas as pd
data= pd.read_csv("all.csv",index_col='num')
words = [word_tokenize(str(item)) for item in data['review']]
from nltk.corpus import stopwords
stop_words = set(stopwords.words("english"))
filterd={1:['']}
li=[]
i=0
for sent in words:
    i=i+1
    for w in sent:
        if w not in stop_words:
            li.append(w)
    filterd.update({i:li})
    li=[]
lema = nltk.wordnet.WordNetLemmatizer()
lemetiz = {1:['']}
li = []
i = 0
for sent in filterd.values():
    i = i+1
    for w in sent:
        li.append(lema.lemmatize(w))
    lemetiz.update({i:li})
    li=[]
try:
    for sent in lemetiz.values():
        ##words = nltk.word_tokenize(sent)
        tag = nltk.pos_tag(sent)
        print(tag)
except Exception as e:
    print(str(e))
