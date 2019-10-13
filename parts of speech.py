# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 18:04:55 2018

@author: Shaheer Akram
"""
"""
POS tag list:
CC coordinating conjunction
CD cardinal digit 
DT determiner 
EX existential there (like: "there is" ... think of it like "there exists")
FW foreign word 
IN preposition/subordinating conjunction
JJ adjective 'big'
JJR adjective, comparative 'bigger'
JJS adjective, superlative 'biggest'
LS list marker 1)
MD modal could, will
NN noun, singular 'desk'
NNS noun plural 'desks'
NNP proper noun, singular 'Harrison'
NNPS proper noun, plural 'Americans'
PDT predeterminer 'all the kids'
POS possessive ending parent's
PRP personal pronoun I, he, she
PRP$ possessive pronoun my, his, hers
RB adverb very, silently, 
RBR adverb, comparative better
RBS adverb, superlative best
RP particle give up
TO to go 'to' the store.
UH interjection errrrrrrrm
VB verb, base form take
VBD verb, past tense took
VBG verb, gerund/present participle taking
VBN verb, past participle taken
VBP verb, sing. present, non-3d take
VBZ verb, 3rd person sing. present takes
WDT wh-determiner which
WP wh-pronoun who, what
WP$ possessive wh-pronoun whose
WRB wh-abverb where, when
"""
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

train = state_union.raw('2005-GWBush.txt')
test = state_union.raw('2006-GWBush.txt')
custom_sent_tokenize = PunktSentenceTokenizer(train)
tokenize = custom_sent_tokenize.tokenize(test)
chunked =[]
try:
    for sent in tokenize:
        words = nltk.word_tokenize(sent)
        tag = nltk.pos_tag(words)
        chunkGram = r"""chunk: {<RB.?>*<VB.?>*<NNP><NN?>}"""
        chunkParser = nltk.RegexpParser(chunkGram)
        ##chunked = chunkParser.parse(tag)
        ##print(chunked)
        ##chunked.draw()
        chunked.append(chunkParser.parse(tag))
        ##print(tag)
except Exception as e:
    print(str(e))
for i in tag:
    if 'VB' in i:
        print(tag)





