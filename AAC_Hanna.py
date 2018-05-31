#!/usr/bin/python
import random
import numpy as np

#Definiendo variables
nota_blanca =[1] 
nota_media = [0.5, 0.5]
nota_negra = [0.25,0.25,0.25,0.25 ]
nota_octava = [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]
nota_dieciseis = [0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625]

blanca_duracion = 1
media_duracion = 0.5
negra_duracion = 0.25
octava_duracion = 0.125
dieciseis_duracion = 0.0625

do_mayor_escala = [0,1,2,3,4,5,6]       #C D E  F G A  B    #0
do_menor_escala = [0,1,2,3,4,5,6]       #C D Eb F G Ab Bb   #1 
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
def selector_tempo(emo_act,emo_pass,pal_total):
    act_max = 0.010
    act_min = -0.002
    act = (emo_act-emo_pass) / pal_total
    _tempo = 40 + (((act - act_min) * (180-40)) / (act_max - act_min))
    return round(_tempo)

#Selección de Octavas Para las 3 melodías
def selector_octavas(pal_alegr,pal_trist,e1,e2,pal_total):
    js_max = 0.0080
    js_min = -0.0080
    js = (pal_alegr - pal_trist) / pal_total

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
    desplazamiento = (max - min) / 5

    for seccion_densidad in densidad: #4 densidades, 1 por sección
        flag = 0
        tmp1 = min
        tmp2 = min + desplazamiento
        if flag != 1 and seccion_densidad >= tmp1 and seccion_densidad < tmp2:
            rhythm_pattern.append(1) #La seccion 1 se toca en una única nota blanca
            flag = 1
        else:
            tmp1 = tmp2 + desplazamiento
        if flag != 1 and seccion_densidad >= tmp2 and seccion_densidad < tmp1:
            rhythm_pattern.append(2)
            flag = 1
        else:
            tmp2 = tmp1 + desplazamiento
        if flag != 1 and seccion_densidad >= tmp1 and seccion_densidad < tmp2:
            rhythm_pattern.append(3)
            flag = 1
        else:
            tmp1 = tmp2 + desplazamiento
        if flag != 1 and seccion_densidad >= tmp2 and seccion_densidad < tmp1:
            rhythm_pattern.append(4)
            flag = 1
        else:
            tmp2 = tmp1 + desplazamiento
        if flag != 1 and seccion_densidad >= tmp1 and seccion_densidad <= max: #No 100 el des encaja
            rhythm_pattern.append(5)
            flag = 1

    return rhythm_pattern

#Random ritmo value:
def random_selector(num_notas,time_signature):
    values_list = []
    patron = []
    value_total = 0
    if num_notas == 1:
        values_list.append(blanca_duracion)
    elif num_notas == 2:
        values_list.append(blanca_duracion)
        values_list.append(media_duracion)
    elif num_notas == 3:
        values_list.append(media_duracion)
        values_list.append(negra_duracion)
    elif num_notas == 4:
        values_list.append(negra_duracion)
        values_list.append(octava_duracion)

    elif num_notas == 5:
         values_list.append(octava_duracion)
         values_list.append(dieciseis_duracion)

    random.shuffle(values_list)
    while value_total < time_signature:
        _r = random.randint(0, len(values_list)-1)
        value_total += values_list[_r]
        patron.append(values_list[_r])    

    if value_total < 1:
        resto = time_signature - value_total
        patron.append(resto)
    elif value_total > 1:
        resto = value_total - time_signature
        patron.remove(resto)

    #Verifica 
    assert (np.sum(patron) == 1)
    return patron
        


#Asigna los valores de c/ ritmo Ejemo oe_list = 2 4 1 1 --> [0.5 0.5 ] [0.25 0.25 0.25 0.25 ] ... so on
def ritmo_value(patron_de_ritmo):
    ritmo_secciones = []
    time_signature = 1
    for seccion in patron_de_ritmo:
        ritmo_pat = []
        if seccion == 1:
            #ritmo_pat = nota_blanca
            ritmo_pat = random_selector(seccion,time_signature)
        elif seccion == 2:
            #ritmo_pat = nota_media
            ritmo_pat = random_selector(seccion,time_signature)
        elif seccion == 3:
            #ritmo_pat = nota_negra
            ritmo_pat = random_selector(seccion,time_signature)
        elif seccion == 4:
            #ritmo_pat = nota_octava
            ritmo_pat = random_selector(seccion,time_signature)
        else:
            #ritmo_pat = nota_dieciseis
            ritmo_pat = random_selector(seccion,time_signature)
        ritmo_secciones.append(ritmo_pat)

    return ritmo_secciones
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
    #print("patron_ritmo ",_patron_ritmo)
    nota_octave = 0.125 
    if _escala == 0:
        escala = do_mayor_escala
    else:
        escala = do_menor_escala

    _melodia = [0] * len(_patron_ritmo)
    for nota in range(0,len(_melodia)):
        if nota == 0 or nota == len(_melodia) -1:
            _n = random.randint(0,2)   
            _melodia[nota] = _acorde[_n]
        elif nota > nota_octave:
            _n = random.randint(0,2)   
            _melodia[nota] = _acorde[_n]
        else:
            if _pitch_contour == 0: #ascendente
                _melodia[nota] = escala[escala.index(_melodia[nota-1] + 1)]
            else: #descendente
                _melodia[nota] = escala[escala.index(_melodia[nota-1] - 1)]
    #print("melodia ",_melodia)
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
    max_e2 = max(e2_list)
    ritmo_e2 = patron_ritmo(min_e2,max_e2,e2_list)
    ritmos_e2 = ritmo_value(ritmo_e2)

    print(ritmo_oe)
    print(ritmo_e1)
    print(ritmo_e2)

    return (ritmos_oe,ritmos_e1,ritmos_e2)
    #La desventaja de esta prueba es: que habrá para c/sec puras notas blancas o negras etc. pero es solo na prueba y es posible
    #que se se solucion con 3 melodias al mismo tiemo
    

#Conversion de Melodia en Notas
def conversion_melodia(_escala,_melodia):
    _patron_melodia = []
    if _escala == 0: #Escala Cmajor
        for _nota in range (0,len(_melodia)):
            _posicion = _melodia[_nota]
            _patron_melodia.append(domayor_escala[_posicion])
    else:
        for _nota in range (0,len(_melodia)):
            _posicion = _melodia[_nota]
            _patron_melodia.append(dominor_escala[_posicion])

    return _patron_melodia

#Conversion de Acordes en Notas
def conversion_acordes(_escala,_acorde):
    _chords = ""
    if _escala == 0:
        for a in range(0,len(_acorde)):
            _chords += domayor_escala[_acorde[a]] 
            if a != len(acorde) - 1:
                _chords += "w+"
    else: 
        for a in range(0,len(_acorde)):
            _chords += dominor_escala[_acorde[a]]
            if a != len(acorde) - 1:
                _chords += "w+"
    _chords += "w"
    return _chords

#Poniendo todo Junto para general un patrón musical
def output(_escala,_tempo,_octava,_melodia,_ritmo,_voz,_acorde):
    voz_melodia = ""
    _measure = " "
    _chords = " "
    if escala == 0:
        voz_melodia += "KCmaj "
    else: 
        voz_melodia += "KCmin "

    _voz = "V"+str(_voz) + " "
    voz_melodia += _voz
    voz_melodia += "T" + str(_tempo) + " "
    _chords += voz_melodia

    for melodia,ritmo in zip(_melodia,_ritmo):
        for nota,tiempo in zip(melodia,ritmo):
            _measure += nota + str(_octava)+"/" + str(tiempo) + "   "
            _chords += _acorde + "   "
        


    #print(voz_melodia + _measure)
    #print(_chords)

    
def values(e1,e2,o0,oe1,oe2,tempo,pos,neg,escala,joy,sad,act,pas,total):
    print("e1: ",e1)
    print("e2: ",e2)
    print("oo: ",o0)
    print("tempo: ",tempo)
    if pos>neg:
        print("Pos/Neg: Positive")
    else:
        print("Negative")
    print("escala: ",escala)
    print("activity: ",(act-pas) / total)
    print("joy/sad: ",joy/total - sad/total)



#Emociones de la novela entera: pan

'''anger =  585
fear =  728
surprise =  445
sadness =  743
joy =  758
dis =  412
antici =  925
trust =  902
pal_positivas =  1465
pal_negativas =  1435
pal_total =  52509
pal_total_emo =  7619
'''


#darck
anger =  651
fear =  911
surprise =  462
sadness =  868
joy =  569
dis =  491
antici =  801
trust =  851
pal_positivas =  1527
pal_negativas =  1617
pal_total =  45933
pal_total_emo =  8560

#theroad
'''
anger =  1046
fear =  1468
surprise =  689
sadness =  1075
joy =  902
dis =  692
antici =  1250
trust =  1173
pal_positivas =  2207
pal_negativas =  2471
pal_total =  77417
pal_total_emo =  13676
'''

e1 = "anticipation"
e2 = "joy"
activas = (joy + anger) 
pasivas = sadness 

escala = selector_escala(pal_positivas,pal_negativas)
acorde = selector_acorde(escala)
tempo = selector_tempo(activas,pasivas,pal_total)
o1,o2,o3 = selector_octavas(joy,sadness,e1,e2,pal_total)

_pitch_contour = escala


values(e1,e2,o1,o2,o3,tempo,pal_positivas,pal_negativas,escala,joy,sadness,activas,pasivas,pal_total)

#Overall Emotion ,e1, e2 (4 secciones)
oe_list = [0.14063690385494437, 0.1287520950784702, 0.14307481334755448, 0.1346944994667073, 0.1497790644522322, 0.13347554472040227, 0.17507237543806187, 0.15529841656516444]
e1_list = [0.022245924120067043, 0.016303519731829957, 0.016455889075118087, 0.016608258418406217, 0.01737010513484687, 0.02148407740362639, 0.02087460003047387, 0.020401948842874544]
e2_list = [0.019350906597592563, 0.016151150388541827, 0.016151150388541827, 0.014779826298948652, 0.016760627761694347, 0.020265122657321347, 0.020417492000609477, 0.0194884287454324]


'''oe_list = [0.18724960808221564, 0.1999651628636126, 0.1785403239853684, 0.1929977355861348, 0.18846890785577425, 0.1633861696568542, 0.19230099285838703, 0.18795683954054995]
e1_list = [0.01933461069500087, 0.021599024560181153, 0.020205539104685595, 0.018637867967253093, 0.023166695697613655, 0.015676711374325032, 0.02368925274342449, 0.026453184824225547]
e2_list = [0.018812053649190037, 0.02037972478662254, 0.01811531092144226, 0.017941125239505314, 0.020205539104685595, 0.015154154328514196, 0.02037972478662254, 0.02419074138531152]
'''
'''
oe_list = [0.19014157280148805, 0.16544383589955564, 0.1858013847266715, 0.15697013537253282, 0.17422754986049396, 0.17856773793531053, 0.16399710654128347, 0.19807811531308123]
e1_list = [0.016017360752299266, 0.018290792601012712, 0.019014157280148807, 0.022630980675829287, 0.020254211015810684, 0.021804278185388035, 0.01798077916709724,0.02521182062409589]
e2_list = [0.015397333884468328, 0.016120698563604423, 0.01653404980882505, 0.013950604526196135, 0.019014157280148807, 0.013640591092280666, 0.015500671695773483,0.019632155404009092]
'''

print(len(oe_list))
print(len(e1_list))
print(len(e2_list))

melodias_oe = []
melodias_e1 = []
melodias_e2 = []

melodias_oe_notas = []
melodias_e1_notas = []
melodias_e2_notas = []

ritmos_oe,ritmos_e1,ritmos_e2 = generator_ritmo(oe_list,e1_list,e2_list)

for ritmo in ritmos_oe:
    melodias_oe.append(selector_nota(acorde,ritmo,escala,_pitch_contour))

for ritmo in ritmos_e1:
    melodias_e1.append(selector_nota(acorde,ritmo,escala,_pitch_contour))

for ritmo in ritmos_e2:
    melodias_e2.append(selector_nota(acorde,ritmo,escala,_pitch_contour))

for melodia in melodias_oe:
    melodia = conversion_melodia(escala,melodia)
    melodias_oe_notas.append(melodia)


for melodia in melodias_e1:
    melodia = conversion_melodia(escala,melodia)
    melodias_e1_notas.append(melodia)


for melodia in melodias_e2:
    melodia = conversion_melodia(escala,melodia)
    melodias_e2_notas.append(melodia)


acorde_nota = conversion_acordes(escala,acorde)
print(acorde_nota)

output(escala,tempo,o1,melodias_oe_notas,ritmos_oe,0,acorde_nota)
output(escala,tempo,o2,melodias_e1_notas,ritmos_e1,1,acorde_nota)
output(escala,tempo,o3,melodias_e2_notas,ritmos_e2,2,acorde_nota)