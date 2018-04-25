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

#Definiendo 8 emociones básicas + 2 sentimientos
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

#Definiendo 8 emociones Avanzadas
optimismo = 0
amor = 0
sumision = 0
susto = 0
decepcion = 0
remordimiento = 0
desprecio = 0
alevosia = 0


#Definiendo scores
num_pal = 0
oe = 0 
e1 = 0 
e2 = 0

#Funcion nrc
def _nrc(pal_novela):
    #print ("Pal analizada:  "+pal_novela)
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
    global optimismo 
    global amor 
    global sumision 
    global susto 
    global decepcion 
    global remordimiento 
    global desprecio 
    global alevosia 
    for emoWord in nrc_lexicon:
        if emoWord[0] == pal_novela:
            if emoWord[1] == "1":
                anger += 1
                #print ("La pal es: anger")
            if emoWord[2] == "1":
                anticipation += 1
                #print ("La pal es: anticipation")
            if emoWord[3] == "1":
                disgust += 1
                #print ("La pal es: disgust")
            if emoWord[4] == "1":
                fear += 1
                #print ("La pal es: fear")
            if emoWord[5] == "1":
                joy += 1
                #print ("La pal es: joy")
            if emoWord[6] == "1":
                negative += 1
                #print ("La pal es: negative: ",pal_novela)
            if emoWord[7] == "1":
                positive += 1
                #print ("La pal es: positive")
            if emoWord[8] == "1":
                sadness += 1
                #print ("La pal es: sadness")
            if emoWord[9] == "1":
                surprise += 1
                #print ("La pal es: surprise")
            if emoWord[10] == "1":
                trust += 1
                #print ("La pal es: trust")
            if emoWord[2] == "1" and emoWord[5] == "1":
                optimismo += 1
            if emoWord[5] == "1" and emoWord[10] == "1":
                amor += 1
            if emoWord[4] == "1" and emoWord[10] == "1":
                sumision += 1
            if emoWord[4] == "1" and emoWord[9] == "1":
                susto += 1
            if emoWord[8] == "1" and emoWord[9] == "1":
                decepcion += 1
            if emoWord[3] == "1" and emoWord[8] == "1":
                remordimiento += 1
            if emoWord[1] == "1" and emoWord[3] == "1":
                desprecio += 1
            if emoWord[1] == "1" and emoWord[2] == "1":
                alevosia += 1

#Leyendo la novela literaria
f = open("/home/danielafe7/Escritorio/NRC_NLTK/Base_Datos/Speeches/steve_4.txt", 'r+')
linea = f.readline()
while linea != "":
    if len(linea) > 1:
            tokens = nltk.word_tokenize(linea)
            for token in tokens:
                if wordnet.synsets(token): #Si la palabra pertenece al diccionario
                    #print(token)    
                    num_pal += 1 
                    _nrc(token)
    linea = f.readline()
f.close()

print ("Pal positives: ",positive)
print ("Pal negatives: ",negative)
print ("Pal anger: ",anger)
print ("Pal fear: ",fear)
print ("Pal surprise: ",surprise)
print ("Pal sadness: ",sadness)
print ("Pal joy: ",joy)
print ("Pal dis: ",disgust)

print ("Pal optimismo: ",optimismo)
print ("Pal amor: ",amor)
print ("Pal sumision: ",sumision)
print ("Pal susto: ",susto)
print ("Pal deception: ",decepcion)
print ("Pal remordimiento: ",remordimiento)
print ("Pal desprecio: ",desprecio)
print ("Pal alevosia: ",alevosia)
print("\n")
print ("Pal antici: ",anticipation)
print ("Pal trust: ",trust)
print ("Pal Total: ",num_pal)