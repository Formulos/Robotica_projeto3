#coding:utf8
from random import randint, choice
import time
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import math
import random
from pf import Particle
from nav_msgs.msg import OccupancyGrid
from occupancy_field import OccupancyField
from helper_functions import angle_normalize, angle_diff
import sys
import os
os.getcwd()
sys.path.append(os.getcwd())

import inspercles
reload(inspercles)

def randow_particle(n_part,minx, miny, maxx, maxy):
    pos = []
    S = []
    for i in range(n_part):
        x = np.random.randint(minx,maxx)
        y = np.random.randint(miny,maxy)
        theta = np.random.randint(0, 2*math.pi)
        p = Particle(x, y, theta)
        S.append(p)
        pos.append([x,y,theta])
        
    S.append(Particle(330, 220, math.radians(90)))
    return S,pos
        

def desvio_pd(pos_particulas,movimento):
    
    S_2 = []
    for i in pos_particulas:
        x = i[0]
        y = i[1]
        theta = i[2]
        x += movimento[0] + np.random.normal(0,1.0)
        y += movimento[1] + np.random.normal(0,1.0)
        theta += movimento[2] + np.random.normal(0,1.0)
        p = Particle(x,y,theta)        
        S_2.append(p)       
    return S_2
            
def calculo_Pdh (valor,leitura,DP = 5):
    result = 1
    for i in (valor):   
        result *= math.e ** (-(leitura[i] - valor[i]) / ((2 * DP) ** 2))
    return result


def normaliza(lista):

    alfa = 1/sum(lista)
    for i in range (len(lista)):
        lista[i] = lista[i] * alfa
    return lista    

def reamostragem(lista_p_normed,particulas):
    for i in range (len(lista_p_normed)):
        particulas[i].w = lista_p_normed[i]
        
        
    particulas_exp = [[p.x, p.y, p.theta] for p in particulas]
    particulas_pesos = [p.w for p in Particle]
    print(particulas_exp)
    print(particulas_exp)
    
def novas_part(particulas,lista_p_normed):
    for i in range(len(particulas)):
        particulas_exp = [[p.x, p.y, p.theta] for p in particulas]
        particulas_pesos = [p.w for p in particulas]
    return particulas_exp, particulas_pesos

def valores_novas_part(novas_particulas):
    for p in novas_particulas:
        p.w = 1
    valores_novas_particulas = [[p.x, p.y, p.theta] for p in novas_particulas]
    return valores_novas_particulas
    
    