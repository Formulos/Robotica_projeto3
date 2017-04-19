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
            
def calculo_Pdh (valor,leitura,DP = 1):
    result = 0
    for i in (valor):     
        print(i)
        print(valor[i])
        dif = -(leitura[i] - valor[i])
        disv = 2*(DP**2)
        result += math.exp(dif/disv)
    return result