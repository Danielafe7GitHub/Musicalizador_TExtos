#!/usr/bin/python
import math
import nltk
from nltk.corpus import wordnet
from nltk.corpus import stopwords
from math import floor

#Cargando nrc_lexicon al vector ncr_lexicon [[palabra,anger,antici,disgu,fear,joy,negati,posi,sadness,surprise,trust],[...]]
n = open("nrc_old_vector.txt", 'r+')
linea = n.readline()
pal_senti_emoci = []
nrc_lexicon = []

#Añadele un enter al ultimo elemento de nrc.txt
while linea != "\n":
    tokens = nltk.word_tokenize(linea)
    for token in tokens:
        pal_senti_emoci.append(token)
    nrc_lexicon.append(pal_senti_emoci)
    pal_senti_emoci = []
    linea = n.readline()
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


#Definiendo scores
num_pal = 0
num_pal_emo = 0
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
    global num_pal_emo 
 
    for emoWord in nrc_lexicon:
        if emoWord[0] == pal_novela:
            num_pal_emo += 1
            if emoWord[1] == "1":
                positive += 1
            if emoWord[2] == "1":
                negative += 1
            if emoWord[3] == "1":
                anger += 1
            if emoWord[4] == "1":
                anticipation += 1
            if emoWord[5] == "1":
                disgust += 1
            if emoWord[6] == "1":
                fear += 1
            if emoWord[7] == "1":
                joy += 1
            if emoWord[8] == "1":
                sadness += 1
            if emoWord[9] == "1":
                surprise += 1
            if emoWord[10] == "1":
                trust += 1
          

#Leyendo la novela literaria
stopWords = set(stopwords.words('english'))
f = open("/home/danielafe7/Escritorio/NRC_NLTK/Base_Datos/Oficial/road_total.txt", 'r+')
linea = f.readline()
while linea != "":
    if len(linea) > 1:
            tokens = nltk.word_tokenize(linea)
            for token in tokens:
                if True:# wordnet.synsets(token): #and (token not in stopWords): #Si la palabra pertenece al diccionario y no es stopword
                    #print(token)    
                    num_pal += 1 
                    _nrc(token)
    linea = f.readline()
f.close()

#Dividiendo la novela en partes
def read_file(cant_pal ,can_texto,total,num_secciones):
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
    global num_pal_emo
    global oe
    global e1
    global e2

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
    num_pal_emo = 0
    oe = 0
    e1 = 0
    e2 = 0

    den_o = []
    den_e1 = []
    den_e2 = []
    f = open("/home/danielafe7/Escritorio/NRC_NLTK/Base_Datos/Oficial/road_total.txt", 'r+')
    linea = f.readline()
    seccion = 1
    t = can_texto
    #print("cant: ",cant_pal)
    #print("parte: ",can_texto)
    
    while linea != "":
        if len(linea) > 1 :
            
            tokens = nltk.word_tokenize(linea)
            for token in tokens:
                
                if True:# wordnet.synsets(token): #and (token not in stopWords): #Si la palabra pertenece al diccionario y no es stopword
                    #print(token) 
                    cant_pal += 1   
                    num_pal += 1 
                    _nrc(token)
                    #print("num: ",num_pal, "cant ",cant_pal)
                if cant_pal == t:
                   #Imprimimos
                    print("-----------------------------------")
                    print("Seccion: ",seccion)
                    print ("anger = ",anger)
                    print ("fear = ",fear)
                    print ("surprise = ",surprise)
                    print ("sadness = ",sadness)
                    print ("joy = ",joy)
                    print ("dis = ",disgust)
                    print ("antici = ",anticipation)
                    print ("trust = ",trust)
                    print ("pal_positivas = ",positive)
                    print ("pal_negativas = ",negative)
                    print ("pal_total = ",num_pal)
                    print ("pal_total_emo = ",num_pal_emo)
                    #Calculando Densidades
                    list_emo = []
                    list_emo.append(anger)
                    list_emo.append(fear)
                    list_emo.append(surprise)
                    list_emo.append(sadness)
                    list_emo.append(joy)
                    list_emo.append(disgust)
                    list_emo.append(anticipation)
                    list_emo.append(trust)

                    list_emo = sorted(list_emo)
                    e1_emo = list_emo[len(list_emo)-1]
                    e2_emo = list_emo[len(list_emo)-2]
                    oe = num_pal_emo / num_pal #overall density
                    e1 = e1_emo / num_pal
                    e2 = e2_emo / num_pal
                    oe = num_pal_emo / num_pal 
                    den_o.append(oe)
                    den_e1.append(e1)
                    den_e2.append(e2)
                    print ("oe: ",oe)
                    print ("e1: ",e1)
                    print ("e2: ",e2)
                    
                    #Reinician los valores
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
                    oe = 0
                    e1 = 0
                    e2 = 0
                    num_pal = 0
                    num_pal_emo = 0
                    cant_pal = t 
                    if seccion == (num_secciones - 1):
                        t = total
                    else:
                        t = t + can_texto
                    seccion += 1
                    #print("cant: ",cant_pal)
                    #print("parte: ",t)
        linea = f.readline()
    print(den_o)
    print(den_e1)
    print(den_e2)
       
    f.close() 


#Obteneindo data info
list_emo = []
list_emo.append(anger)
list_emo.append(fear)
list_emo.append(surprise)
list_emo.append(sadness)
list_emo.append(joy)
list_emo.append(disgust)
list_emo.append(anticipation)
list_emo.append(trust)

list_emo = sorted(list_emo)
e1_emo = list_emo[len(list_emo)-1]
e2_emo = list_emo[len(list_emo)-2]
oe = num_pal_emo / num_pal #overall density
e1 = e1_emo / num_pal
e2 = e2_emo / num_pal



print ("anger = ",anger)
print ("fear = ",fear)
print ("surprise = ",surprise)
print ("sadness = ",sadness)
print ("joy = ",joy)
print ("dis = ",disgust)
print ("antici = ",anticipation)
print ("trust = ",trust)
print ("pal_positivas = ",positive)
print ("pal_negativas = ",negative)
print ("pal_total = ",num_pal)
print ("pal_total_emo = ",num_pal_emo)
print("\n")

num_secciones = 8
read_file(0,floor(num_pal/num_secciones),num_pal,num_secciones)
'''print ("Overal density: ",oe,",")
print ("e1 density: ",e1,",")
print ("e2 density: ",e2,",")'''


'''print("\n")

print ("Pal optimismo: ",optimismo)
print ("Pal amor: ",amor)
print ("Pal sumision: ",sumision)
print ("Pal susto: ",susto)
print ("Pal deception: ",decepcion)
print ("Pal remordimiento: ",remordimiento)
print ("Pal desprecio: ",desprecio)
print ("Pal alevosia: ",alevosia)
print("\n")'''
