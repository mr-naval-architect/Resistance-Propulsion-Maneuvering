import matplotlib.pyplot as plt
import numpy as np


from Input import LengthWL
from Input import Beam
from Input import Draught

from Input import CB
from Input import LCB

from Input import Volume

from Input import RoSalt

from Input import AppendageCoef

from Input import SpeedMS
from Input import SpeedCruisingMS
from Input import FroudeNo
from Input import FroudeNoCruising

from Wetted_Surface import S

from Friction_Res import FrictionCoef
from Friction_Res import FrictionCoefCruising
from Friction_Res import FrictionRes
from Friction_Res import FrictionResCruising

# ======================================================================================================================
# SSPA - APPROXIMATE RESISTANCE AND POWER PREDICTION METHOD
# ======================================================================================================================


if CB < 0.625:
    LCBs = 8.499945 - 40.999807 * CB + 39.999832 * CB**2
elif 0.625 <= CB:
    LCBs = 27.093853 - 102.000307 * CB + 90.000227 * CB**2


if CB < 0.6:
#    f = open('ResCoef\\SSPA_Coef\\SSPAResRegCoefCB_525_600.csv', 'r')
    f = open('SSPAResRegCoefCB_525_600.csv', 'r')
    fn18 = list()
    fn19 = list()
    fn20 = list()
    fn21 = list()
    fn22 = list()
    fn23 = list()
    fn24 = list()
    fn25 = list()
    fn26 = list()
    fn27 = list()
    fn28 = list()
    fn29 = list()
    fn30 = list()

    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.replace(',', '.')
        line = line.split(";")
        fn18.append(float(line[0]))
        fn19.append(float(line[1]))
        fn20.append(float(line[2]))
        fn21.append(float(line[3]))
        fn22.append(float(line[4]))
        fn23.append(float(line[5]))
        fn24.append(float(line[6]))
        fn25.append(float(line[7]))
        fn26.append(float(line[8]))
        fn27.append(float(line[9]))
        fn28.append(float(line[10]))
        fn29.append(float(line[11]))
        fn30.append(float(line[12]))
    f.close()

elif 0.6 <= CB < 0.625:
#    f = open('ResCoef\\SSPA_Coef\\SSPAResRegCoefCB_600_625.csv', 'r')
    f = open('SSPAResRegCoefCB_600_625.csv', 'r')
    fn18 = list()
    fn19 = list()
    fn20 = list()
    fn21 = list()
    fn22 = list()
    fn23 = list()
    fn24 = list()
    fn25 = list()
    fn26 = list()
    fn27 = list()
    fn28 = list()
    fn29 = list()
    fn30 = list()

    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.replace(',', '.')
        line = line.split(";")
        fn18.append(float(line[0]))
        fn19.append(float(line[1]))
        fn20.append(float(line[2]))
        fn21.append(float(line[3]))
        fn22.append(float(line[4]))
        fn23.append(float(line[5]))
        fn24.append(float(line[6]))
        fn25.append(float(line[7]))
        fn26.append(float(line[8]))
        fn27.append(float(line[9]))
        fn28.append(float(line[10]))
        fn29.append(float(line[11]))
        fn30.append(float(line[12]))
    f.close()

elif 0.625 <= CB < 0.65:
#    f = open('ResCoef\\SSPA_Coef\\SSPAResRegCoefCB_625_650.csv', 'r')
    f = open('SSPAResRegCoefCB_625_650.csv', 'r')
    fn18 = list()
    fn19 = list()
    fn20 = list()
    fn21 = list()
    fn22 = list()
    fn23 = list()
    fn24 = list()
    fn25 = list()
    fn26 = list()
    fn27 = list()
    fn28 = list()
    fn29 = list()
    fn30 = list()

    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.replace(',', '.')
        line = line.split(";")
        fn18.append(float(line[0]))
        fn19.append(float(line[1]))
        fn20.append(float(line[2]))
        fn21.append(float(line[3]))
        fn22.append(float(line[4]))
        fn23.append(float(line[5]))
        fn24.append(float(line[6]))
        fn25.append(float(line[7]))
        fn26.append(float(line[8]))
        fn27.append(float(line[9]))
        fn28.append(float(line[10]))
        fn29.append(float(line[11]))
        fn30.append(float(line[12]))
    f.close()

elif 0.65 <= CB < 0.675:
#    f = open('ResCoef\\SSPA_Coef\\SSPAResRegCoefCB_650_675.csv', 'r')
    f = open('SSPAResRegCoefCB_650_675.csv', 'r')
    fn18 = list()
    fn19 = list()
    fn20 = list()
    fn21 = list()
    fn22 = list()
    fn23 = list()
    fn24 = list()
    fn25 = list()
    fn26 = list()
    fn27 = list()
    fn28 = list()
    fn29 = list()
    fn30 = list()

    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.replace(',', '.')
        line = line.split(";")
        fn18.append(float(line[0]))
        fn19.append(float(line[1]))
        fn20.append(float(line[2]))
        fn21.append(float(line[3]))
        fn22.append(float(line[4]))
        fn23.append(float(line[5]))
        fn24.append(float(line[6]))
        fn25.append(float(line[7]))
        fn26.append(float(line[8]))
        fn27.append(float(line[9]))
        fn28.append(float(line[10]))
        fn29.append(float(line[11]))
        fn30.append(float(line[12]))
    f.close()

elif 0.675 <= CB < 0.7:
#    f = open('ResCoef\\SSPA_Coef\\SSPAResRegCoefCB_675_700.csv', 'r')
    f = open('SSPAResRegCoefCB_675_700.csv', 'r')
    fn18 = list()
    fn19 = list()
    fn20 = list()
    fn21 = list()
    fn22 = list()
    fn23 = list()
    fn24 = list()
    fn25 = list()
    fn26 = list()
    fn27 = list()
    fn28 = list()
    fn29 = list()
    fn30 = list()

    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.replace(',', '.')
        line = line.split(";")
        fn18.append(float(line[0]))
        fn19.append(float(line[1]))
        fn20.append(float(line[2]))
        fn21.append(float(line[3]))
        fn22.append(float(line[4]))
        fn23.append(float(line[5]))
        fn24.append(float(line[6]))
        fn25.append(float(line[7]))
        fn26.append(float(line[8]))
        fn27.append(float(line[9]))
        fn28.append(float(line[10]))
        fn29.append(float(line[11]))
        fn30.append(float(line[12]))
    f.close()

elif 0.7 <= CB:
#    f = open('ResCoef\\SSPA_Coef\\SSPAResRegCoefCB_700_725.csv', 'r')
    f = open('SSPAResRegCoefCB_700_725.csv', 'r')
    fn18 = list()
    fn19 = list()
    fn20 = list()
    fn21 = list()
    fn22 = list()
    fn23 = list()
    fn24 = list()
    fn25 = list()
    fn26 = list()
    fn27 = list()
    fn28 = list()
    fn29 = list()
    fn30 = list()

    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.replace(',', '.')
        line = line.split(";")
        fn18.append(float(line[0]))
        fn19.append(float(line[1]))
        fn20.append(float(line[2]))
        fn21.append(float(line[3]))
        fn22.append(float(line[4]))
        fn23.append(float(line[5]))
        fn24.append(float(line[6]))
        fn25.append(float(line[7]))
        fn26.append(float(line[8]))
        fn27.append(float(line[9]))
        fn28.append(float(line[10]))
        fn29.append(float(line[11]))
        fn30.append(float(line[12]))
    f.close()

print (fn18)
print (fn19)
print (fn20)
print (fn21)
print (fn22)
print (fn23)
print (fn24)
print (fn25)
print (fn26)
print (fn27)
print (fn28)
print (fn29)
print (fn30)


a = list()
i = 0
l = len(fn18)

while i < l:
    if FroudeNoCruising < 0.18:
        a.append(fn18[i] + (FroudeNoCruising - 0.18) * (fn19[i] - fn18[i]) / (0.19 - 0.18))
    elif 0.18 <= FroudeNoCruising < 0.19:
        a.append(fn18[i] + (FroudeNoCruising - 0.18) * (fn19[i] - fn18[i]) / (0.19 - 0.18))
    elif 0.19 <= FroudeNoCruising < 0.20:
        a.append(fn19[i] + (FroudeNoCruising - 0.19) * (fn20[i] - fn19[i]) / (0.20 - 0.19))
    elif 0.20 <= FroudeNoCruising < 0.21:
        a.append(fn20[i] + (FroudeNoCruising - 0.20) * (fn21[i] - fn20[i]) / (0.21 - 0.20))
    elif 0.21 <= FroudeNoCruising < 0.22:
        a.append(fn21[i] + (FroudeNoCruising - 0.21) * (fn22[i] - fn21[i]) / (0.22 - 0.21))
    elif 0.22 <= FroudeNoCruising < 0.23:
        a.append(fn22[i] + (FroudeNoCruising - 0.22) * (fn23[i] - fn22[i]) / (0.23 - 0.22))
    elif 0.23 <= FroudeNoCruising < 0.24:
        a.append(fn23[i] + (FroudeNoCruising - 0.23) * (fn24[i] - fn23[i]) / (0.24 - 0.23))
    elif 0.24 <= FroudeNoCruising < 0.25:
        a.append(fn24[i] + (FroudeNoCruising - 0.24) * (fn25[i] - fn24[i]) / (0.25 - 0.24))
    elif 0.25 <= FroudeNoCruising < 0.26:
        a.append(fn25[i] + (FroudeNoCruising - 0.25) * (fn26[i] - fn25[i]) / (0.26 - 0.25))
    elif 0.26 <= FroudeNoCruising < 0.27:
        a.append(fn26[i] + (FroudeNoCruising - 0.26) * (fn27[i] - fn26[i]) / (0.27 - 0.26))
    elif 0.27 <= FroudeNoCruising < 0.28:
        a.append(fn27[i] + (FroudeNoCruising - 0.27) * (fn28[i] - fn27[i]) / (0.28 - 0.27))
    elif 0.28 <= FroudeNoCruising < 0.29:
        a.append(fn28[i] + (FroudeNoCruising - 0.28) * (fn29[i] - fn28[i]) / (0.29 - 0.28))
    elif 0.29 <= FroudeNoCruising < 0.30:
        a.append(fn29[i] + (FroudeNoCruising - 0.29) * (fn30[i] - fn29[i]) / (0.30 - 0.29))
    elif 0.30 <= FroudeNoCruising:
        a.append(fn29[i] + (FroudeNoCruising - 0.29) * (fn30[i] - fn29[i]) / (0.30 - 0.29))
    i += 1



CR_Cruising = (a[0] + a[1] * CB + a[2] * CB**2 + a[3] * CB**3 + a[4] * (LengthWL / (Volume**(1 / 3))) + a[5] * (LengthWL / (Volume**(1 / 3)))**2 + a[6] * (LengthWL / (Volume**(1 / 3)))**3 + a[7] * CB * (LengthWL / (Volume**(1 / 3))) + a[8] * CB**2 * (LengthWL / (Volume**(1 / 3))) + a[9] * CB * (LengthWL / (Volume**(1 / 3)))**2 + a[10] * (Beam / Draught - 2.4) + a[11] * CB * (Beam / Draught - 2.4) + a[12] * (LCB - LCBs) + a[13] * CB * (LCB - LCBs) + a[14] * (LCB**2 - LCBs**2) + a[15] * CB * (LCB**2 - LCBs **2)) / 1000

ReainingResSSPACruising = 0.5 * RoSalt * S * SpeedCruisingMS**2 * CR_Cruising

CorelationResSSPACruising = 0.5 * RoSalt * S * SpeedCruisingMS**2 * AppendageCoef

TotalResSSPACruising = ReainingResSSPACruising + CorelationResSSPACruising + FrictionResCruising

print (TotalResSSPACruising)


# ======================================================================================================================

j = 0
k = len(FroudeNo)

CR = list()

while j < k:

    a = list()
    i = 0
    l = len(fn18)

    while i < l:
        if FroudeNo[j] < 0.18:
            a.append(fn18[i] + (FroudeNo[j] - 0.18) * (fn19[i] - fn18[i]) / (0.19 - 0.18))
        elif 0.18 <= FroudeNo[j] < 0.19:
            a.append(fn18[i] + (FroudeNo[j] - 0.18) * (fn19[i] - fn18[i]) / (0.19 - 0.18))
        elif 0.19 <= FroudeNo[j] < 0.20:
            a.append(fn19[i] + (FroudeNo[j] - 0.19) * (fn20[i] - fn19[i]) / (0.20 - 0.19))
        elif 0.20 <= FroudeNo[j] < 0.21:
            a.append(fn20[i] + (FroudeNo[j] - 0.20) * (fn21[i] - fn20[i]) / (0.21 - 0.20))
        elif 0.21 <= FroudeNo[j] < 0.22:
            a.append(fn21[i] + (FroudeNo[j] - 0.21) * (fn22[i] - fn21[i]) / (0.22 - 0.21))
        elif 0.22 <= FroudeNo[j] < 0.23:
            a.append(fn22[i] + (FroudeNo[j] - 0.22) * (fn23[i] - fn22[i]) / (0.23 - 0.22))
        elif 0.23 <= FroudeNo[j] < 0.24:
            a.append(fn23[i] + (FroudeNo[j] - 0.23) * (fn24[i] - fn23[i]) / (0.24 - 0.23))
        elif 0.24 <= FroudeNo[j] < 0.25:
            a.append(fn24[i] + (FroudeNo[j] - 0.24) * (fn25[i] - fn24[i]) / (0.25 - 0.24))
        elif 0.25 <= FroudeNo[j] < 0.26:
            a.append(fn25[i] + (FroudeNo[j] - 0.25) * (fn26[i] - fn25[i]) / (0.26 - 0.25))
        elif 0.26 <= FroudeNo[j] < 0.27:
            a.append(fn26[i] + (FroudeNo[j] - 0.26) * (fn27[i] - fn26[i]) / (0.27 - 0.26))
        elif 0.27 <= FroudeNo[j] < 0.28:
            a.append(fn27[i] + (FroudeNo[j] - 0.27) * (fn28[i] - fn27[i]) / (0.28 - 0.27))
        elif 0.28 <= FroudeNo[j] < 0.29:
            a.append(fn28[i] + (FroudeNo[j] - 0.28) * (fn29[i] - fn28[i]) / (0.29 - 0.28))
        elif 0.29 <= FroudeNo[j] < 0.30:
            a.append(fn29[i] + (FroudeNo[j] - 0.29) * (fn30[i] - fn29[i]) / (0.30 - 0.29))
        elif 0.30 <= FroudeNo[j]:
            a.append(fn29[i] + (FroudeNo[j] - 0.29) * (fn30[i] - fn29[i]) / (0.30 - 0.29))
        i += 1

    CR.append((a[0] + a[1] * CB + a[2] * CB ** 2 + a[3] * CB ** 3 + a[4] * (LengthWL / (Volume ** (1 / 3))) + a[
        5] * (LengthWL / (Volume ** (1 / 3))) ** 2 + a[6] * (LengthWL / (Volume ** (1 / 3))) ** 3 + a[7] * CB * (
                               LengthWL / (Volume ** (1 / 3))) + a[8] * CB ** 2 * (LengthWL / (Volume ** (1 / 3))) + a[
                       9] * CB * (LengthWL / (Volume ** (1 / 3))) ** 2 + a[10] * (Beam / Draught - 2.4) + a[11] * CB * (
                               Beam / Draught - 2.4) + a[12] * (LCB - LCBs) + a[13] * CB * (LCB - LCBs) + a[14] * (
                               LCB ** 2 - LCBs ** 2) + a[15] * CB * (LCB ** 2 - LCBs ** 2)) / 1000)

    j += 1



ReainingResSSPA = 0.5 * RoSalt * S * SpeedMS ** 2 * CR

CorelationResSSPA = 0.5 * RoSalt * S * SpeedMS ** 2 * AppendageCoef

TotalResSSPA = ReainingResSSPA + CorelationResSSPA + FrictionRes


#plt.plot(SpeedMS, FrictionRes)
#plt.plot(SpeedMS, CorelationResSSPA)
#plt.plot(SpeedMS, ReainingResSSPA)
#plt.plot(SpeedMS, TotalResSSPA)
#plt.xticks()
#plt.yticks()
#plt.ylabel("Resistance R [kN]")
#plt.xlabel("Speed V [m/s]")
#plt.grid()
#plt.show()

