#!/usr/bin/python
import math
import random
import numpy as np

blanca_duracion = 1
media_duracion = 0.5
negra_duracion = 0.25
octava_duracion = 0.125
dieciseis_duracion = 0.0625

def random_selector(num_notas,time_signature):
    values_list = []
    patron = []
    value_total = 0
    #if num = 1 pick values {blanca}
    if num_notas == 1:
        values_list.append(blanca_duracion)
    #if num = 2 pick values {blanca,media}
    elif num_notas == 2:
        values_list.append(blanca_duracion)
        values_list.append(media_duracion)
    #if num = 3 pick values {media,negra}
    elif num_notas == 3:
        values_list.append(media_duracion)
        values_list.append(negra_duracion)
    #if num = 4 pick values {negra,ocho}
    elif num_notas == 4:
        values_list.append(negra_duracion)
        values_list.append(octava_duracion)

    elif num_notas == 5:
         values_list.append(octava_duracion)
         values_list.append(dieciseis_duracion)

    random.shuffle(values_list)
    print("Lista valores: ",values_list)
    #Con la lista de valores llena, contruirmos un patrón que de como total = 1 (time_signature)
    while value_total < time_signature:
        _r = random.randint(0, len(values_list)-1)
        print("_r: ",_r)
        value_total += values_list[_r]
        patron.append(values_list[_r])
    

    
    print("Lista valores Patron: ",patron)
    if value_total == 1:
        print("Done: ",value_total)
    elif value_total < 1:
        #Escoge una nota, cualquiera que complete el patron 
        resto = time_signature - value_total
        print("total: ",value_total, " add: ",resto)
        patron.append(resto)
    elif value_total > 1:
        #Escoge una nota, se resta el patron
        resto = value_total - time_signature
        print("total: ",value_total, " resto: ",resto)
        patron.remove(resto)
        print("Lista valores Patron: ",patron)

    #Verifica 
    assert (np.sum(patron) == 1)


#Init
time_signature = 1

random_selector(1,time_signature)
random_selector(2,time_signature)
random_selector(3,time_signature)
random_selector(4,time_signature)
random_selector(5,time_signature)
