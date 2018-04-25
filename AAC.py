#!/usr/bin/python
import random

#12-Notas Piano (non-octava) : do,reb,re,mib,mi,fa,solb,sol,lab,la,sib,si
notas_piano_nombre = ["do","reb","re","mib","mi","fa","solb","sol","lab","la","sib","si"]
notas_piano = [1,2,3,4,5,6,7,8,9,10,11,12]
do_mayor_escala = [1,3,5,6,8,10,12] #do,re,mi,fa,sol,la,si     #0
do_menor_escala = [1,3,4,6,8,9,11] #do,re,mib,fa,sol,lab,sib   #1 

#Cmajor Key 7 chords


#Modulo Armonía Markov_Matrix
Markov_Matrix = [[0,       0.05,   0.07,   0.35,   0.35,   0.08,   0.1],
                 [0.05,    0,      0.05,   0.15,   0.65,   0.2,    0],
                 [0,       0.07,   0,      0.2,    0.8,    0.65,   0],
                 [0.15,    0.15,   0.05,   0,      0.6,    0.05,   0],
                 [0.64,    0.05,   0.05,   0.13,   0,      0.13,   0],
                 [0.06,    0.35,   0.12,   0.12,   0.35,   0,      0],
                 [1,       0,      0,      0,      0,      0,      0]]

#Se elige una anota aleatoria y se va iterando la matriz
def selector_acorde(escala):
    _acorde = []
    _grado = random.randint(0, 6)   
    #print("Grado: ",_grado) 
    _nota_base = Markov_Matrix[_grado].index(max(Markov_Matrix[_grado])) #Se elige la nota base más probable 
    #print("NotaBase: ",_nota_base) 
    if escala == 0 :
        _acorde.append(do_mayor_escala[_nota_base])  #Nota base
        _acorde.append(do_mayor_escala[(_nota_base + 2) % 7])  #Su tercera
        _acorde.append(do_mayor_escala[(_nota_base + 4) % 7])  #Su quinta

    return _acorde

#Modulo Ritmo :Factores (Densidad/complejidad)

#1. Time Signature: 4/4 por ahora, ver luego una orma de que la duracion se acople al Tsignature
time_signature = 4 

#2. Note value selection

duracion_notas = [1,2,3,4,5] #whole, half, quarter, eight, and sixteenth
nota_blanca = 1   # 1
nota_media = 0.5  # 2
nota_negra = 0.25 # 3
nota_octava = 0.125 # 4
nota_dieciseis = 0.0625 # 5

def random_value_selector(_complejidad,_densidad):
    rhythmic_pattern = []
    if _complejidad >=0 and _complejidad <= 0.49 and _densidad >=0.5 and _densidad <=0.79:  #Retorna valores de solo negras/medias
        _r = random.randint(2, 3)
        if _r == 2:
            return [0.5,0.5]
        else: 
            return [0.25,0.25,0.25,0.25]
    elif _complejidad >=0 and _complejidad <= 0.49 and _densidad >=0.8 and _densidad <=1:   #Retorna valores de solo 1/8 ó 1/16, media siempre y cuando la suma cumpla 1
         _r = random.randint(4,5)
         if _r == 4:
                         return [0.125,0.125,0.125,0.125,0.125,0.125,0.125,0.125]
         else: 
             return [0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625,0.0625]

    elif _complejidad >=0.5 and _complejidad <= 0.79 and _densidad >=0 and _densidad <=0.4: #Retorna values entre blancas/media
        _duracion = 0
        while _duracion <1:
            _r = random.randint(1,2)
            if _r == 1:
                rhythmic_pattern.append(nota_blanca)
                _duracion += nota_blanca
            else:
                 rhythmic_pattern.append(nota_media)
                 _duracion += nota_media

    elif _complejidad >=0.5 and _complejidad <= 0.79 and _densidad >=0.5 and _densidad <=0.79: #Retorna valores entre medias/ negras
        _duracion = 0
        while _duracion <1:
            _r = random.randint(2,3)
            if _r == 2:
                rhythmic_pattern.append(nota_media)
                _duracion += nota_media
            else:
                 rhythmic_pattern.append(nota_negra)
                 _duracion += nota_negra

    
    elif  _complejidad >=0.5 and _complejidad <= 0.79 and _densidad >=0.8 and _densidad <=1: #Retorna valores entre 1/16, 1/8
        _duracion = 0
        while _duracion <1:
            _r = random.randint(4,5)
            if _r == 4:
                rhythmic_pattern.append(nota_octava)
                _duracion += nota_octava
            else:
                 rhythmic_pattern.append(nota_dieciseis)
                 _duracion += nota_dieciseis


    elif _complejidad >=0.8 and _complejidad <= 1 and _densidad >=0 and _densidad <=0.49: #Retorna values entre blancas/media
        _duracion = 0
        while _duracion <1:
            _r = random.randint(1,2)
            if _r == 1:
                rhythmic_pattern.append(nota_blanca)
                _duracion += nota_blanca
            else:
                 rhythmic_pattern.append(nota_media)
                 _duracion += nota_media


    elif _complejidad >=0.8 and _complejidad <= 1 and _densidad >=0.5 and _densidad <=0.79: #Retorna valores entre negras/ ó medias ó 1/18
        _duracion = 0
        while _duracion <1:
            _r = random.randint(2,4)
            if _r == 2:
                rhythmic_pattern.append(nota_media)
                _duracion += nota_blanca
            elif _r == 3:
                rhythmic_pattern.append(nota_negra)
                _duracion += nota_negra
            else:
                 rhythmic_pattern.append(nota_octava)
                 _duracion += nota_octava

    elif _complejidad >=0.8 and _complejidad <= 1 and _densidad >=0.8 and _densidad <=1: #Retorna valores entre 1/16, 1/8 / negras
        _duracion = 0
        while _duracion <1:
            _r = random.randint(3,5)
            if _r == 3:
                rhythmic_pattern.append(nota_negra)
                _duracion += nota_negra
            elif _r == 3:
                rhythmic_pattern.append(nota_octava)
                _duracion += nota_octava
            else:
                 rhythmic_pattern.append(nota_dieciseis)
                 _duracion += nota_dieciseis
    print("La duracion total es: ",_duracion)
    return rhythmic_pattern
        

def note_value_selection(_ts,_densidad,_complejidad):
    patron_ritmo = []
    # Si no es muy complejo y no muy denso ; no hay variacion de notas y son de larga duracion    
    if _complejidad >=0 and _complejidad <= 0.49 and _densidad >=0 and _densidad <=0.49:
        patron_ritmo.append(1)
        #print("caso 1")
        return patron_ritmo #Retorna una nota blanca

    # Si no es muy complejo y medianamente denso 
    if _complejidad >=0 and _complejidad <= 0.49 and _densidad >=0.5 and _densidad <=0.79:
        patron_rimtmo = random_value_selector(_complejidad,_densidad)
        #print("caso 2")
        return patron_rimtmo 
    
    # Si no es muy complejo y muy denso
    if _complejidad >=0 and _complejidad <= 0.49 and _densidad >=0.8 and _densidad <=1:
        patron_ritmo = random_value_selector(_complejidad,_densidad) 
        #print("caso 3")
        return patron_ritmo 

    # Si es medianamente complejo y no muy denso
    if _complejidad >=0.5 and _complejidad <= 0.79 and _densidad >=0 and _densidad <=0.49:
        patron_ritmo = random_value_selector(_complejidad,_densidad) 
        #print("caso 4")
        return patron_ritmo 

    # Si es medianamente complejo y medianamente denso
    if _complejidad >=0.5 and _complejidad <= 0.79 and _densidad >=0.5 and _densidad <=0.79:
        patron_ritmo = random_value_selector(_complejidad,_densidad) 
        #print("caso 5")
        return patron_ritmo 
    
    # Si es medianamente complejo y muy denso
    if _complejidad >=0.5 and _complejidad <= 0.79 and _densidad >=0.8 and _densidad <=1:
        patron_ritmo = random_value_selector(_complejidad,_densidad) 
        #print("caso 6")
        return patron_ritmo 


    # Si es muy complejo  y no muy denso    
    if _complejidad >=0.8 and _complejidad <= 1 and _densidad >=0 and _densidad <=0.49:
        patron_ritmo = random_value_selector(_complejidad,_densidad) 
        #print("caso 7")
        return patron_ritmo 

    # Si es muy complejo  y medianamente denso 
    if _complejidad >=0.8 and _complejidad <= 1 and _densidad >=0.5 and _densidad <=0.79:
        patron_ritmo = random_value_selector(_complejidad,_densidad) 
        #print("caso 8")
        return patron_ritmo 

    # Si es muy complejo y muy denso
    if _complejidad >=0.8 and _complejidad <= 1 and _densidad >=0.8 and _densidad <=1:
        patron_ritmo = random_value_selector(_complejidad,_densidad)  
        #print("caso 9")
        return patron_ritmo
    


#Modulo Melodia
def selector_nota(_acorde,_patron_ritmo,_escala,_pitch_contour):
    if _escala == 0:
        escala = do_mayor_escala
    else:
        escala = do_menor_escala

    _melodia = _patron_ritmo
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

 

#Selección de Escala 0 escala mayor , 1 escala menor
def selector_escala(pal_positivas,pal_negativas):
    _ratio = pal_positivas / pal_negativas
    if _ratio > 1:
        return 0
    else:
        return 1

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

#Selección Tempo 40bmp -180bpm
def selector_tempo(emo_act,emo_pass):
    act_max = 0.017
    act_min = -0.002
    act = emo_act - emo_pass
    _tempo = 40 + (((act - act_min) * (180-40)) / (act_max - act_min))
    return round(_tempo)

#Init :Parámetros Ladrón Bicicletas (Pruebas basadas en 8 emo básicas)
cant_emo_total = 485
cant_pal_total = 3768

positivas = 128
negativas = 126
positivas_s1 = 29
negativas_s1 = 13
positivas_s2 = 55
negativas_s2 = 52
positivas_s3 = 44
negativas_s3 = 61
#Densidades de las Secciones Apoach Improvisado
d1 = 0.2 #Densidad General Sección 1
d1_m1 = 0.9
d1_m2 = 0.2
d2 = 0.8 #Densidad M1 Sección 2
d2_m1 = 0.5
d1_m2 = 0.6
d3 = 0.5 #Densidad M2 Sección 3
d3_m1 = 0.2
d1_m2 = 1

#JS de toda la novela : e1,e2 : emoción + presente en la novela
alegria = 49 / cant_pal_total
tristeza = 66 / cant_pal_total
e1 = "anticipation"
e2 = "trust"

#Complejidad de las Secciones
c1 =  round(random.uniform(0.0, 1.0),2)
c3 = (random.uniform(0,1))
c2 = (random.uniform(0,1))


enfado = 52 
activas = (alegria + enfado) / cant_pal_total #Nota / pal_total
pasivas = tristeza / cant_pal_total
#densidad = 0
#conplejidad = 0

#Parametros Toda Novela
escala = selector_escala(positivas,negativas)
tempo = selector_tempo(activas,pasivas)
oo,om1,om2 = selector_octavas(alegria,tristeza,e1,e2) #C/melodía se toca en su respectiva Octava - probar cambiar de octava x measure
if escala == 0:
    print ("KCmaj")
else: 
    print ("KCmin")
print("T",str(tempo))
print(str(oo),"  ",str(om1)," ",str(om2))

#Calculando Bar/mesure (1) Sección 1 Melodía 1
print("Bar (1)")
acorde = selector_acorde(escala) #Falta cadences y duración del acorde #cuidado Aleatorio!!!
pitch_contour_s1 = selector_escala(positivas_s1,negativas_s1) #Estamos probando por sección
patron_ritmo = note_value_selection(1,d1,c1) #Probando Complejidad Aleatoria y para toda la sección 
melodia = selector_nota(acorde,patron_ritmo,escala,pitch_contour_s1)


print("acorde ",acorde)
print("pitch count ",pitch_contour_s1)
print("patron_ritmico ",patron_ritmo)
print("melodia ",melodia)


#Calculando Bar/mesure (2) Sección 1 Melodía 1
print("Bar (2)")
acorde = selector_acorde(escala) #Falta cadences y duración del acorde #cuidado Aleatorio!!!
pitch_contour_s1 = selector_escala(positivas_s1,negativas_s1) #Estamos probando por sección
patron_ritmo = note_value_selection(1,d1,c1) #Probando Complejidad Aleatoria y para toda la sección 
melodia = selector_nota(acorde,patron_ritmo,escala,pitch_contour_s1)


print("acorde ",acorde)
print("pitch count ",pitch_contour_s1)
print("patron_ritmico ",patron_ritmo)
print("melodia ",melodia)

#Calculando Bar/mesure (3) Sección 1 Melodía 1
print("Bar (3)")
acorde = selector_acorde(escala) #Falta cadences y duración del acorde #cuidado Aleatorio!!!
pitch_contour_s1 = selector_escala(positivas_s1,negativas_s1) #Estamos probando por sección
patron_ritmo = note_value_selection(1,d1,c1) #Probando Complejidad Aleatoria y para toda la sección 
melodia = selector_nota(acorde,patron_ritmo,escala,pitch_contour_s1)


print("acorde ",acorde)
print("pitch count ",pitch_contour_s1)
print("patron_ritmico ",patron_ritmo)
print("melodia ",melodia)










#Calculando Bar/mesure (2) Sección 1 Melodía 1
print("Bar (1)")
acorde = selector_acorde(escala) #Falta cadences y duración del acorde #cuidado Aleatorio!!!
pitch_contour_s2 = selector_escala(positivas_s2,negativas_s2) #Estamos probando por sección
patron_ritmo = note_value_selection(1,d2,c2) #Probando Complejidad Aleatoria y para toda la sección 
melodia = selector_nota(acorde,patron_ritmo,escala,pitch_contour_s2)


print("acorde ",acorde)
print("pitch count ",pitch_contour_s1)
print("patron_ritmico ",patron_ritmo)
print("melodia ",melodia)


#Calculando Bar/mesure (2) Sección 1 Melodía 1
print("Bar (2)")
acorde = selector_acorde(escala) #Falta cadences y duración del acorde #cuidado Aleatorio!!!
pitch_contour_s2 = selector_escala(positivas_s2,negativas_s2) #Estamos probando por sección
patron_ritmo = note_value_selection(1,d2,c2) #Probando Complejidad Aleatoria y para toda la sección 
melodia = selector_nota(acorde,patron_ritmo,escala,pitch_contour_s2)



print("acorde ",acorde)
print("pitch count ",pitch_contour_s2)
print("patron_ritmico ",patron_ritmo)
print("melodia ",melodia)

#Calculando Bar/mesure (3) Sección 1 Melodía 1
print("Bar (3)")
acorde = selector_acorde(escala) #Falta cadences y duración del acorde #cuidado Aleatorio!!!
pitch_contour_s2 = selector_escala(positivas_s2,negativas_s2) #Estamos probando por sección
patron_ritmo = note_value_selection(1,d2,c2) #Probando Complejidad Aleatoria y para toda la sección 
melodia = selector_nota(acorde,patron_ritmo,escala,pitch_contour_s2)


print("acorde ",acorde)
print("pitch count ",pitch_contour_s2)
print("patron_ritmico ",patron_ritmo)
print("melodia ",melodia)











#Calculando Bar/mesure (2) Sección 1 Melodía 1
print("Bar (1)")
acorde = selector_acorde(escala) #Falta cadences y duración del acorde #cuidado Aleatorio!!!
pitch_contour_s3 = selector_escala(positivas_s3,negativas_s3) #Estamos probando por sección
patron_ritmo = note_value_selection(1,d3,c3) #Probando Complejidad Aleatoria y para toda la sección 
melodia = selector_nota(acorde,patron_ritmo,escala,pitch_contour_s3)


print("acorde ",acorde)
print("pitch count ",pitch_contour_s3)
print("patron_ritmico ",patron_ritmo)
print("melodia ",melodia)


#Calculando Bar/mesure (2) Sección 1 Melodía 1
print("Bar (2)")
acorde = selector_acorde(escala) #Falta cadences y duración del acorde #cuidado Aleatorio!!!
pitch_contour_s3 = selector_escala(positivas_s3,negativas_s3) #Estamos probando por sección
patron_ritmo = note_value_selection(1,d3,c3) #Probando Complejidad Aleatoria y para toda la sección 
melodia = selector_nota(acorde,patron_ritmo,escala,pitch_contour_s3)


print("acorde ",acorde)
print("pitch count ",pitch_contour_s3)
print("patron_ritmico ",patron_ritmo)
print("melodia ",melodia)




#Calculando Bar/mesure (3) Sección 1 Melodía 1
print("Bar (3)")
acorde = selector_acorde(escala) #Falta cadences y duración del acorde #cuidado Aleatorio!!!
pitch_contour_s3 = selector_escala(positivas_s3,negativas_s3) #Estamos probando por sección
patron_ritmo = note_value_selection(1,d3,c3) #Probando Complejidad Aleatoria y para toda la sección 
melodia = selector_nota(acorde,patron_ritmo,escala,pitch_contour_s3)


print("acorde ",acorde)
print("pitch count ",pitch_contour_s3)
print("patron_ritmico ",patron_ritmo)
print("melodia ",melodia)




#Objetivo Melodía 1
#KCmaj  V0 T180 A6/0.25 D6/0.125 F6/0.25 B6/0.25 B6/0.125 B6/0.25
