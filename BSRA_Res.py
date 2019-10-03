import matplotlib.pyplot as plt
import numpy as np


from Input import LengthWL
from Input import LengthPP
from Input import Beam
from Input import Draught

from Input import CB
from Input import LCB

from Input import Volume
from Input import Displacement
#
from Input import RoSalt
#
#from Input import AppendageCoef
#
from Input import SpeedMS
from Input import SpeedCruisingMS
#from Input import FroudeNo
#from Input import FroudeNoCruising
#
from Wetted_Surface import S
#
#from Friction_Res import FrictionCoef
#from Friction_Res import FrictionCoefCruising
#from Friction_Res import FrictionRes
#from Friction_Res import FrictionResCruising

# ======================================================================================================================
# BSRA - APPROXIMATE RESISTANCE AND POWER PREDICTION METHOD
# ======================================================================================================================


LengthWLft = LengthWL * 3.28084

x1 = 1
x2 = ((LengthPP / (Volume**(1/3))) - 5.296) / 1.064
x3 = 10 * (Beam / Draught - 3.025) / 9.05
x4 = 1000 * (CB - 0.725) / 75
x5 = (LCB - 0.77) / 2.77
x6 = x2**2
x7 = x3**2
x8 = x4**2
x9 = x5**2
x10 = x2 * x3
x11 = x2 * x4
x12 = x2 * x5
x13 = x3 * x4
x14 = x3 * x5
x15 = x4 * x5
x16 = x5 * x4**2

V_L_Cruising = SpeedCruisingMS / (LengthPP ** 0.5)

a = list()

#f = open('ResCoef\\BSRA_Coef\\BSRAResistanceRegCoef.csv', 'r')
f = open('BSRAResistanceRegCoef.csv', 'r')
a050 = list()
a055 = list()
a060 = list()
a065 = list()
a070 = list()
a075 = list()
a080 = list()


lines = f.readlines()
for line in lines:
    line = line.strip()
    line = line.replace(',', '.')
    line = line.split(";")
    a050.append(float(line[0]))
    a055.append(float(line[1]))
    a060.append(float(line[2]))
    a065.append(float(line[3]))
    a070.append(float(line[4]))
    a075.append(float(line[5]))
    a080.append(float(line[6]))
f.close()

l = len(a050)

i = 0

while (i < l):
    if V_L_Cruising < 0.5:
        a.append(a050[i] + (V_L_Cruising - 0.50) * (a055[i] - a050[i]) / (0.55 - 0.5))
    elif 0.5 <= V_L_Cruising < 0.55:
        a.append(a050[i] + (V_L_Cruising - 0.50) * (a055[i] - a050[i]) / (0.55 - 0.5))
    elif 0.55 <= V_L_Cruising < 0.6:
        a.append(a055[i] + (V_L_Cruising - 0.55) * (a060[i] - a055[i]) / (0.60 - 0.55))
    elif 0.60 <= V_L_Cruising < 0.65:
        a.append(a060[i] + (V_L_Cruising - 0.60) * (a065[i] - a060[i]) / (0.65 - 0.60))
    elif 0.65 <= V_L_Cruising < 0.70:
        a.append(a065[i] + (V_L_Cruising - 0.65) * (a070[i] - a065[i]) / (0.70 - 0.65))
    elif 0.70 <= V_L_Cruising < 0.75:
        a.append(a070[i] + (V_L_Cruising - 0.70) * (a075[i] - a070[i]) / (0.75 - 0.70))
    elif 0.75 <= V_L_Cruising < 0.80:
        a.append(a075[i] + (V_L_Cruising - 0.75) * (a080[i] - a075[i]) / (0.80 - 0.75))
    elif 0.80 <= V_L_Cruising:
        a.append(a075[i] + (V_L_Cruising - 0.75) * (a080[i] - a075[i]) / (0.80 - 0.75))
    i += 1

Y400Cruising = a[0] * x1 + a[1] * x2 + a[2] * x3 + a[3] * x4 + a[4] * x5 + a[5] * x6 + a[6] * x7 + a[7] * x8 + a[8] * x9 + a[9] * x10 + a[10] * x11 + a[11] * x12 + a[12] * x13 + a[13] * x14 + a[14] * x15 + a[15] * x16

CR400Cruising = 5.1635 * Y400Cruising + 13.1035

CRounded400Cruising = (CR400Cruising * (SpeedCruisingMS / (LengthWL**(1 / 2)))) / (2.4938 * (LengthPP / (Volume**(1 / 3))))


k_list = list()

#f = open('ResCoef\\BSRA_Coef\\BSRACorrectiveCoef.csv', 'r')
f = open('BSRACorrectiveCoef.csv', 'r')
k06 = list()
k08 = list()
k10 = list()
k12 = list()
k14 = list()



lines = f.readlines()
for line in lines:
    line = line.strip()
    line = line.replace(',', '.')
    line = line.split(";")
    k06.append(float(line[0]))
    k08.append(float(line[1]))
    k10.append(float(line[2]))
    k12.append(float(line[3]))
    k14.append(float(line[4]))
f.close()

l = len(k06)

i = 0

while (i < l):
    if V_L_Cruising < 0.6:
        k_list.append(k06[i] + (V_L_Cruising - 0.6) * (k08[i] - k06[i]) / (0.8 - 0.6))
    elif 0.6 <= V_L_Cruising < 0.8:
        k_list.append(k06[i] + (V_L_Cruising - 0.6) * (k08[i] - k06[i]) / (0.8 - 0.6))
    elif 0.8 <= V_L_Cruising < 1.0:
        k_list.append(k08[i] + (V_L_Cruising - 0.8) * (k10[i] - k08[i]) / (1.0 - 0.8))
    elif 1.0 <= V_L_Cruising < 1.2:
        k_list.append(k10[i] + (V_L_Cruising - 1.0) * (k12[i] - k10[i]) / (1.2 - 1.0))
    elif 1.2 <= V_L_Cruising < 1.4:
        k_list.append(k12[i] + (V_L_Cruising - 1.2) * (k14[i] - k12[i]) / (1.4 - 1.2))
    elif 1.4 <= V_L_Cruising:
        k_list.append(k12[i] + (V_L_Cruising - 1.2) * (k14[i] - k12[i]) / (1.4 - 1.2))
    i += 1


if LengthWLft < 100.0:
    k = k_list[0] + (LengthWLft - 100) * (k_list[1] - k_list[0]) / (150 - 100)
elif 100.0 <= LengthWLft < 150.0:
    k = k_list[0] + (LengthWLft - 100) * (k_list[1] - k_list[0]) / (150 - 100)
elif 150.0 <= LengthWLft < 200.0:
    k = k_list[1] + (LengthWLft - 150) * (k_list[2] - k_list[1]) / (200 - 150)
elif 200.0 <= LengthWLft < 250.0:
    k = k_list[2] + (LengthWLft - 200) * (k_list[3] - k_list[2]) / (250 - 200)
elif 250.0 <= LengthWLft < 300.0:
    k = k_list[3] + (LengthWLft - 250) * (k_list[4] - k_list[3]) / (300 - 250)
elif 300.0 <= LengthWLft < 350.0:
    k = k_list[4] + (LengthWLft - 300) * (k_list[5] - k_list[4]) / (350 - 300)
elif 350.0 <= LengthWLft < 400.0:
    k = k_list[5] + (LengthWLft - 350) * (k_list[6] - k_list[5]) / (400 - 350)
elif 400.0 <= LengthWLft < 450.0:
    k = k_list[6] + (LengthWLft - 400) * (k_list[7] - k_list[6]) / (450 - 400)
elif 450.0 <= LengthWLft < 500.0:
    k = k_list[7] + (LengthWLft - 450) * (k_list[8] - k_list[7]) / (500 - 450)
elif 500.0 <= LengthWLft < 550.0:
    k = k_list[8] + (LengthWLft - 500) * (k_list[9] - k_list[8]) / (550 - 500)
elif 550.0 <= LengthWLft < 600.0:
    k = k_list[9] + (LengthWLft - 550) * (k_list[10] - k_list[9]) / (600 - 550)
elif 600.0 <= LengthWLft < 650.0:
    k = k_list[10] + (LengthWLft - 600) * (k_list[11] - k_list[10]) / (650 - 600)
elif 650.0 <= LengthWLft < 700.0:
    k = k_list[11] + (LengthWLft - 650) * (k_list[12] - k_list[11]) / (700 - 650)
elif 700.0 <= LengthWLft < 750.0:
    k = k_list[12] + (LengthWLft - 700) * (k_list[13] - k_list[12]) / (750 - 700)
elif 750.0 <= LengthWLft < 800.0:
    k = k_list[13] + (LengthWLft - 750) * (k_list[14] - k_list[13]) / (800 - 750)
elif 800.0 <= LengthWLft < 850.0:
    k = k_list[14] + (LengthWLft - 800) * (k_list[15] - k_list[14]) / (850 - 800)
elif 850.0 <= LengthWLft < 900.0:
    k = k_list[15] + (LengthWLft - 850) * (k_list[16] - k_list[15]) / (900 - 850)
elif 900.0 <= LengthWLft < 950.0:
    k = k_list[16] + (LengthWLft - 900) * (k_list[17] - k_list[16]) / (950 - 900)
elif 950.0 <= LengthWLft < 1000.0:
    k = k_list[17] + (LengthWLft - 950) * (k_list[18] - k_list[17]) / (1000 - 950)
elif 1000.0 <= LengthWLft:
    k = k_list[17] + (LengthWLft - 950) * (k_list[18] - k_list[17]) / (1000 - 950)

CRoundedCruising = CRounded400Cruising + k * (S / (Volume**(2 / 3)))

CR_Cruising = 2.4938 * CRoundedCruising * LengthPP / (Volume**(1 / 3))

TotalResBSRACruising = 5.045 * 10**(-3) * ((Displacement * SpeedCruisingMS**2) / LengthPP) * CR_Cruising

print('Resistance at cruising speed by BSRA =', TotalResBSRACruising, '[kN]')

# ======================================================================================================================
# BSRA - APPROXIMATE RESISTANCE AND POWER PREDICTION METHOD FOR A RANGE OF SPEEDS
# ======================================================================================================================


V_L = SpeedMS / (LengthPP ** 0.5)

a = list()

TotalResBSRA = list()

p = len(V_L)
n = 0


while n < p:

    l = len(a050)

    i = 0

    while (i < l):

        if V_L[n] < 0.5:
            a.append(a050[i] + (V_L[n] - 0.50) * (a055[i] - a050[i]) / (0.55 - 0.5))
        elif 0.5 <= V_L[n] < 0.55:
            a.append(a050[i] + (V_L[n] - 0.50) * (a055[i] - a050[i]) / (0.55 - 0.5))
        elif 0.55 <= V_L[n] < 0.6:
            a.append(a055[i] + (V_L[n] - 0.55) * (a060[i] - a055[i]) / (0.60 - 0.55))
        elif 0.60 <= V_L[n] < 0.65:
            a.append(a060[i] + (V_L[n] - 0.60) * (a065[i] - a060[i]) / (0.65 - 0.60))
        elif 0.65 <= V_L[n] < 0.70:
            a.append(a065[i] + (V_L[n] - 0.65) * (a070[i] - a065[i]) / (0.70 - 0.65))
        elif 0.70 <= V_L[n] < 0.75:
            a.append(a070[i] + (V_L[n] - 0.70) * (a075[i] - a070[i]) / (0.75 - 0.70))
        elif 0.75 <= V_L[n] < 0.80:
            a.append(a075[i] + (V_L[n] - 0.75) * (a080[i] - a075[i]) / (0.80 - 0.75))
        elif 0.80 <= V_L[n]:
            a.append(a075[i] + (V_L[n] - 0.75) * (a080[i] - a075[i]) / (0.80 - 0.75))
        i += 1


    Y400 = a[0] * x1 + a[1] * x2 + a[2] * x3 + a[3] * x4 + a[4] * x5 + a[5] * x6 + a[6] * x7 + a[7] * x8 + a[8] * x9 + a[9] * x10 + a[10] * x11 + a[11] * x12 + a[12] * x13 + a[13] * x14 + a[14] * x15 + a[15] * x16

    CR400 = 5.1635 * Y400 + 13.1035

    CRounded400 = (CR400 * (SpeedMS[n] / (LengthWL**(1 / 2)))) / (2.4938 * (LengthPP / (Volume**(1 / 3))))


    l = len(k06)

    i = 0


    while (i < l):

        if V_L[n] < 0.6:
            k_list.append(k06[i] + (V_L[n] - 0.6) * (k08[i] - k06[i]) / (0.8 - 0.6))
        elif 0.6 <= V_L[n] < 0.8:
            k_list.append(k06[i] + (V_L[n] - 0.6) * (k08[i] - k06[i]) / (0.8 - 0.6))
        elif 0.8 <= V_L[n] < 1.0:
            k_list.append(k08[i] + (V_L[n] - 0.8) * (k10[i] - k08[i]) / (1.0 - 0.8))
        elif 1.0 <= V_L[n] < 1.2:
            k_list.append(k10[i] + (V_L[n] - 1.0) * (k12[i] - k10[i]) / (1.2 - 1.0))
        elif 1.2 <= V_L[n] < 1.4:
            k_list.append(k12[i] + (V_L[n] - 1.2) * (k14[i] - k12[i]) / (1.4 - 1.2))
        elif 1.4 <= V_L[n]:
            k_list.append(k12[i] + (V_L[n] - 1.2) * (k14[i] - k12[i]) / (1.4 - 1.2))
        i += 1


    if LengthWLft < 100.0:
        k = k_list[0] + (LengthWLft - 100) * (k_list[1] - k_list[0]) / (150 - 100)
    elif 100.0 <= LengthWLft < 150.0:
        k = k_list[0] + (LengthWLft - 100) * (k_list[1] - k_list[0]) / (150 - 100)
    elif 150.0 <= LengthWLft < 200.0:
        k = k_list[1] + (LengthWLft - 150) * (k_list[2] - k_list[1]) / (200 - 150)
    elif 200.0 <= LengthWLft < 250.0:
        k = k_list[2] + (LengthWLft - 200) * (k_list[3] - k_list[2]) / (250 - 200)
    elif 250.0 <= LengthWLft < 300.0:
        k = k_list[3] + (LengthWLft - 250) * (k_list[4] - k_list[3]) / (300 - 250)
    elif 300.0 <= LengthWLft < 350.0:
        k = k_list[4] + (LengthWLft - 300) * (k_list[5] - k_list[4]) / (350 - 300)
    elif 350.0 <= LengthWLft < 400.0:
        k = k_list[5] + (LengthWLft - 350) * (k_list[6] - k_list[5]) / (400 - 350)
    elif 400.0 <= LengthWLft < 450.0:
        k = k_list[6] + (LengthWLft - 400) * (k_list[7] - k_list[6]) / (450 - 400)
    elif 450.0 <= LengthWLft < 500.0:
        k = k_list[7] + (LengthWLft - 450) * (k_list[8] - k_list[7]) / (500 - 450)
    elif 500.0 <= LengthWLft < 550.0:
        k = k_list[8] + (LengthWLft - 500) * (k_list[9] - k_list[8]) / (550 - 500)
    elif 550.0 <= LengthWLft < 600.0:
        k = k_list[9] + (LengthWLft - 550) * (k_list[10] - k_list[9]) / (600 - 550)
    elif 600.0 <= LengthWLft < 650.0:
        k = k_list[10] + (LengthWLft - 600) * (k_list[11] - k_list[10]) / (650 - 600)
    elif 650.0 <= LengthWLft < 700.0:
        k = k_list[11] + (LengthWLft - 650) * (k_list[12] - k_list[11]) / (700 - 650)
    elif 700.0 <= LengthWLft < 750.0:
        k = k_list[12] + (LengthWLft - 700) * (k_list[13] - k_list[12]) / (750 - 700)
    elif 750.0 <= LengthWLft < 800.0:
        k = k_list[13] + (LengthWLft - 750) * (k_list[14] - k_list[13]) / (800 - 750)
    elif 800.0 <= LengthWLft < 850.0:
        k = k_list[14] + (LengthWLft - 800) * (k_list[15] - k_list[14]) / (850 - 800)
    elif 850.0 <= LengthWLft < 900.0:
        k = k_list[15] + (LengthWLft - 850) * (k_list[16] - k_list[15]) / (900 - 850)
    elif 900.0 <= LengthWLft < 950.0:
        k = k_list[16] + (LengthWLft - 900) * (k_list[17] - k_list[16]) / (950 - 900)
    elif 950.0 <= LengthWLft < 1000.0:
        k = k_list[17] + (LengthWLft - 950) * (k_list[18] - k_list[17]) / (1000 - 950)
    elif 1000.0 <= LengthWLft:
        k = k_list[17] + (LengthWLft - 950) * (k_list[18] - k_list[17]) / (1000 - 950)

    CRounded = CRounded400 + k * (S / (Volume**(2 / 3)))

    CR = 2.4938 * CRounded * LengthPP / (Volume**(1 / 3))

    TotalResBSRAiter = 5.045 * 10**(-3) * ((Displacement * (SpeedMS[n])**2) / LengthPP) * CR

    TotalResBSRA.append(TotalResBSRAiter)

    n += 1

print('Resistance by BSRA =', TotalResBSRA, '[kN]')


#plt.plot(SpeedMS, TotalResBSRA)
#plt.xticks()
#plt.yticks()
#plt.ylabel("Resistance R [kN]")
#plt.xlabel("Speed V [m/s]")
#plt.grid()
#plt.show()





















