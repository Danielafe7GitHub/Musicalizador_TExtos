#!/usr/bin/python
import random

#Definiendo variables
nota_blanca =[1] 
nota_media = [0.5, 0.5]
nota_negra = [0.25,0.25,0.25,0.25 ]
nota_octava = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]
nota_dieciseis = [0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625]

domayor_escala = ["C","D","E","F","G","A","B"] 
dominor_escala = ["C","D","Eb","F","G","Ab","Bb"] 
grado_acorde = ["I", "II", "III", "IV", "V", "VI", "VII"]

#Modulo Armonía Markov_Matrix
Markov_Matrix = [[0,       0.05,   0.07,   0.35,   0.35,   0.08,   0.1],
                 [0.05,    0,      0.05,   0.15,   0.65,   0.2,    0],
                 [0,       0.07,   0,      0.2,    0.8,    0.65,   0],
                 [0.15,    0.15,   0.05,   0,      0.6,    0.05,   0],
                 [0.64,    0.05,   0.05,   0.13,   0,      0.13,   0],
                 [0.06,    0.35,   0.12,   0.12,   0.35,   0,      0],
                 [1,       0,      0,      0,      0,      0,      0]]


#Selección de Escala 0 escala mayor , 1 escala menor
def selector_escala(pal_positivas,pal_negativas):
    _ratio = pal_positivas / pal_negativas
    if _ratio > 1:
        return 0
    else:
        return 1

#Selección Tempo 40bmp -180bpm
def selector_tempo(emo_act,emo_pass):
    act_max = 0.017
    act_min = -0.002
    act = emo_act - emo_pass
    _tempo = 40 + (((act - act_min) * (180-40)) / (act_max - act_min))
    return round(_tempo)

#Selección de Octavas Para las 3 melodías
def selector_octavas(pal_alegr,pal_trist,e1,e2):
    js_max = 0.017
    js_min = -0.002
    js = pal_alegr - pal_trist
    _octava  = 4 + round((js - js_min)*(6-4)/(js_max - js_min))

    if e1 == "joy" or e1 == "trust":
        _octava_m1 =  _octava + 1
    elif e1 == "anger" or e1 == "fear" or e1 == "sadness" or e1 == "disgust":
        _octava_m1 =  _octava - 1

    else:
        _octava_m1 = _octava

    if e2 == "joy" or e2 == "trust":
        _octava_m2 =  _octava + 1
    elif e2 == "anger" or e2 == "fear" or e2 == "sadness" or e2 == "disgust":
        _octava_m2 =  _octava - 1

    else:
        _octava_m2 = _octava

    return _octava,_octava_m1,_octava_m2

#Devuelve una lista del numero de notas que tiene c/seccion Ejemo oe_list = 2 4 1 1 --> 2 notas para secc1 4 notas secc 2 ... so on
def patron_ritmo(min,max,densidad):
    rhythm_pattern = []
    desplazamiento = (min+max) / 5
    for seccion_densidad in densidad:
        tmp1 = min
        tmp2 = min + desplazamiento

        if seccion_densidad >= tmp1 and seccion_densidad < tmp2:
            rhythm_pattern.append(1) #La seccion 1 se toca en una única nota blanca
        tmp1 = tmp2 + desplazamiento
        elif seccion_densidad >= tmp2 and seccion_densidad < tmp1:
            rhythm_pattern.append(2)
        tmp2 = tmp1 + desplazamiento
        elif seccion_densidad >= tmp1 and seccion_densidad < tmp2:
            rhythm_pattern.append(3)
        tmp1 = tmp2 + desplazamiento
        elif seccion_densidad >= tmp2 and seccion_densidad < tmp1:
            rhythm_pattern.append(4)
        tmp2 = tmp1 + desplazamiento
        elif seccion_densidad >= tmp1 and seccion_densidad <= tmp2:
            rhythm_pattern.append(5)
        else: 
            print("Error al asignar duracion values ")

    return rhythm_pattern

#Asigna los valores de c/ ritmo Ejemo oe_list = 2 4 1 1 --> [0.5 0.5 ] [0.25 0.25 0.25 0.25 ] ... so on
def ritmo_value(patron_de_ritmo):
    ritmo_secciones = []
    ritmo_pat = []
    for seccion in patron_de_ritmo:
        if seccion == 1:
            ritmo_pat = nota_blanca
        elif seccion == 2:
            ritmo_pat = nota_media
        elif seccion == 3:
            ritmo_pat = nota_negra
        elif seccion == 4:
            ritmo_pat = nota_octava
        else:
            ritmo_pat = nota_dieciseis
        ritmo_secciones.append(ritmo_pat)
        ritmo_pat.clear()

#Generación de Melodías (Mo,Me1,Me2)

#Modulo Armonía (Se elige una anota aleatoria y se va iterando la matriz)
def selector_acorde(escala):
    _acorde = []
    _grado = random.randint(0, 6)   
    #print("Grado: ",_grado) 
    _nota_base = Markov_Matrix[_grado].index(max(Markov_Matrix[_grado])) #Se elige la nota base más probable 
    print("Acorde: ",grado_acorde[_nota_base]) 
    if escala == 0 :
        _acorde.append(do_mayor_escala[_nota_base])  #Nota base
        _acorde.append(do_mayor_escala[(_nota_base + 2) % 7])  #Su tercera
        _acorde.append(do_mayor_escala[(_nota_base + 4) % 7 ])  #Su quinta
    else:
        _acorde.append(do_menor_escala[_nota_base])  #Nota base
        _acorde.append(do_menor_escala[(_nota_base + 2) % 7])  #Su tercera
        _acorde.append(do_menor_escala[(_nota_base + 4) % 7 ])  #Su quinta

    return _acorde


#Modulo Melodia (Ponerle notas al ritmo)
def selector_nota(_acorde,_patron_ritmo,_escala,_pitch_contour):
    if _escala == 0:
        escala = do_mayor_escala
    else:
        escala = do_menor_escala

    _melodia = [0] * len(_patron_ritmo)
    for nota in range(0,len(_melodia)):
        if nota == 0 or nota == len(_melodia) -1:
            _n = random.randint(0,2)   
            _melodia[nota] = _acorde[_n]
        elif nota > nota_octava:
            _n = random.randint(0,2)   
            _melodia[nota] = _acorde[_n]
        else:
            if _pitch_contour == 0: #ascendente
                _melodia[nota] = escala[escala.index(_melodia[nota-1] + 1)]
            else: #descendente
                _melodia[nota] = escala[escala.index(_melodia[nota-1] - 1)]

    return _melodia



#Modulo Ritmo
def generator_ritmo(oe_list,e1_list,e2_list):
    #We first split the interval between the maximum and minimum emotion density for the novel into five equal parts
    min_oe = min(oe_list)
    max_oe = max(oe_list)
    ritmo_oe = patron_ritmo(min_oe,max_oe,oe_list)
    ritmos_oe = ritmo_value(ritmo_oe) #4 patrones de ritmo, uno para cada seccion

    min_e1 = min(e1_list)
    max_e1 = max(e1_list)
    ritmo_e1 = patron_ritmo(min_e1,max_e1,e1_list)
    ritmos_e1 = ritmo_value(ritmo_e1)


    min_e2 = min(e2_list)
    max_e2 = miax(e2_list)
    ritmo_e2 = patron_ritmo(min_e2,max_e2,e2_list)
    ritmos_e2 = ritmo_value(ritmo_e2)

    return (ritmos_oe,ritmos_e1,ritmos_e2)
    #La desventaja de esta prueba es: que habrá para c/sec puras notas blancas o negras etc. pero es solo na prueba y es posible
    #que se se solucion con 3 melodias al mismo tiemo
    

#Emociones de la novela entera
anger =  585
fear =  728
surprise =  445
sadness =  743
joy =  776
dis = 412
antici =  925
trust =  920

#Init
pal_positivas = 1473
pal_negativas = 1435
pal_total = 29940
pal_total_emo = 7627
activas = (joy + anger) / pal_total #Nota / pal_total
pasivas = sadness / pal_total
e1 = "anticipation"
e2 = "trust"

escala = selector_escala(pal_positivas,pal_negativas)
tempo = selector_tempo(activas,pasivas)
o1,o2,o3 = selector_octavas(joy,sadness,e1,e2)
_pitch_contour = escala


#Overall Emotion ,e1, e2 (4 secciones)
oe_list = [0.24028738690792975,0.24248145650708025,0.24715110256030784,0.28514299563742124]
e1_list = [0.03139968068121341,0.029534726904922454,0.03270682255438804,0.03562772661173049]
e2_list = [0.03100053219797765,0.023465947403910992,0.031818854521237235,0.0340523509452254]

melodias_oe = []
melodias_e1 = []
melodias_e2 = []

ritmos_oe,ritmos_e1,ritmos_e2 = generator_ritmo(oe_list,e1_list,e2_list)
for ritmo in ritmos_oe:
    melodias_oe.append(selector_nota(acorde,ritmo,escala,_pitch_contour))

for ritmo in ritmos_e1:
    melodias_oe.append(selector_nota(acorde,ritmo,escala,_pitch_contour))

for ritmo in ritmos_e2:
    melodias_oe.append(selector_nota(acorde,ritmo,escala,_pitch_contour))

