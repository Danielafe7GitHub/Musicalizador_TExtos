#!/usr/bin/python
import math
import nltk
from nltk.corpus import wordnet

#Cargando nrc_lexicon al vector ncr_lexicon [[palabra,anger,antici,disgu,fear,joy,negati,posi,sadness,surprise,trust],[...]]
n = open("nrc.txt", 'r+')
linea = n.readline()
pal_senti_emoci = []
nrc_lexicon = []
pal_pivote = "aback"
pal_senti_emoci.append(pal_pivote)

#Añadele un enter al ultimo elemento de nrc.txt
while linea != "\n":
    tokens = nltk.word_tokenize(linea)
    if tokens[0] == pal_pivote:
        pal_senti_emoci.append(tokens[2])
    else:
        nrc_lexicon.append(pal_senti_emoci)
        pal_senti_emoci = []
        pal_pivote = tokens[0]
        pal_senti_emoci.append(pal_pivote)
        pal_senti_emoci.append(tokens[2])
    linea = n.readline()
nrc_lexicon.append(pal_senti_emoci)
n.close()

positive = 0
negative = 0
print("Num Pal_ NRC: ",len(nrc_lexicon))
for i in range(0,len(nrc_lexicon)):
    if nrc_lexicon[i][6] == "1":
        positive = positive + 1
    if nrc_lexicon[i][7] == "1":
        negative = negative + 1

print ("Hay Pal POsi: ",positive)
print ("Hay Pal Nega: ",negative)