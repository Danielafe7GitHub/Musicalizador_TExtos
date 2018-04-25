#!/usr/bin/python
import math
import nltk

#Cargando nrc_lexicon Español al vector ncr_lexicon [[palabra,anger,antici,disgu,fear,joy,negati,posi,sadness,surprise,trust],[...]]
n = open("spanish.txt", 'r+')
linea = n.readline()
pal_senti_emoci = []
nrc_lexicon = []
pal_pivote = "detrás"
pal_senti_emoci.append(pal_pivote)

#Añadele un enter al ultimo elemento de nrc.txt
while linea != "\n":
    tokens = nltk.word_tokenize(linea)
    if tokens[0] == pal_pivote:
        for i in range(1,11):
            pal_senti_emoci.append(tokens[i])
    else:
        nrc_lexicon.append(pal_senti_emoci)
        pal_senti_emoci = []
        pal_pivote = tokens[0]
        pal_senti_emoci.append(pal_pivote)
        for i in range(1,11):
            pal_senti_emoci.append(tokens[i])
    linea = n.readline()
nrc_lexicon.append(pal_senti_emoci)
n.close()

#Definiendo scores 
positive = 0 
negative = 0
anger = 0 
fear = 0 
anticipation = 0 
trust = 0 
surprise = 0 
sadness = 0 
joy = 0  
disgust = 0
num_pal = 0
oe = 0 
e1 = 0 
e2 = 0

#Funcion nrc
def _nrc(pal_novela):
    print ("Pal analizada:  "+pal_novela)
    global positive 
    global negative 
    global anger  
    global fear  
    global anticipation 
    global trust 
    global surprise 
    global sadness 
    global joy  
    global disgust
    global num_pal 
    for emoWord in nrc_lexicon:
        if emoWord[0] == pal_novela:
            if emoWord[1] == "1":
                positive += 1
                print ("La pal es: positive")
            if emoWord[2] == "1":
                negative += 1
                print ("La pal es: negative")
            if emoWord[3] == "1":
                anger += 1
                print ("La pal es: anger")
            if emoWord[4] == "1":
                anticipation += 1
                print ("La pal es: anticipation")
            if emoWord[5] == "1":
                disgust += 1
                print ("La pal es: disgust")
            if emoWord[6] == "1":
                fear += 1
                print ("La pal es: fear")
            if emoWord[7] == "1":
                joy += 1
                print ("La pal es: joy")
            if emoWord[8] == "1":
                sadness += 1
                print ("La pal es: sadness")
            if emoWord[9] == "1":
                surprise += 1
                print ("La pal es: surprise")
            if emoWord[10] == "1":
                trust += 1
                print ("La pal es: trust")

#Leyendo la novela literaria
f = open("peterS.txt", 'r+')
linea = f.readline()
while linea != "":
    if len(linea) > 1:
            tokens = nltk.word_tokenize(linea)
            for token in tokens:
                num_pal += 1
                _nrc(token)
    linea = f.readline()
f.close()

print ("Pal positives: ",positive)
print ("Pal negatives: ",negative)
print ("Pal anger: ",anger)
print ("Pal fear: ",fear)
print ("Pal antici: ",anticipation)
print ("Pal trust: ",trust)
print ("Pal surprise: ",surprise)
print ("Pal sadness: ",sadness)
print ("Pal joy: ",joy)
print ("Pal dis: ",disgust)
print ("Pal Total: ",num_pal)
