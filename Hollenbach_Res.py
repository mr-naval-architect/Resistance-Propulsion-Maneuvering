import matplotlib.pyplot as plt
import numpy as np


from Input import LengthDEP
from Input import LengthWL
from Input import LengthPP
from Input import Beam
from Input import Draught
from Input import DraughtFore
from Input import DraughtStern

from Input import CB

from Input import RoSalt

from Input import D
from Input import NoPropellers

from Input import NoRudders
from Input import NoBraces
from Input import NoBossings
from Input import NoThrusters

from Input import SpeedMS
from Input import SpeedCruisingMS
from Input import FroudeNoLDep
from Input import FroudeNoLDepCruising

from Input import AppendageCoef

from Wetted_Surface import S

from Friction_Res import FrictionRes
from Friction_Res import FrictionResCruising


# ======================================================================================================================
# HOLLENBACH - APPROXIMATE RESISTANCE AND POWER PREDICTION METHOD
# ======================================================================================================================

#f = open('ResCoef\\HollenbachResistanceRegCoef.csv', 'r')
f = open('HollenbachResistanceRegCoef.csv', 'r')
a = list()

# I am not considering ships with more then two propellers.
# I suppose this method can give an aroximation of resistance for those ships using the coefficients for two proppeler ship.
# This method can easily be expanded to calculate resistance in balast condition, but that can be done in the future.


if NoPropellers == 1:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.replace(',', '.')
        line = line.split(";")
        a.append(float(line[0]))  # For fully loaded single propeller ships
    f.close()
else:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.replace(',', '.')
        line = line.split(";")
        a.append(float(line[2]))  # For two propeller ships
    f.close()


#print (a)


def RemainingResHol(a, LengthPP, CB, FroudeNoLDep, Draught, Beam, LengthDEP, LengthWL, DraughtStern, DraughtFore, D, NoRudders, NoBraces, NoBossings, NoThrusters, RoSalt, SpeedMS):
    kL = a[22] * (LengthPP**a[23])
    FroudeNo_krit = a[19] + (a[20] * CB) + (a[21] * (CB**2))
    CR_Fn_krit = np.maximum(1.0, (FroudeNoLDep / FroudeNo_krit)**(FroudeNoLDep / FroudeNo_krit))
    CR_standard = a[10] + a[11] * FroudeNoLDep + a[12] * (FroudeNoLDep**2) + CB * (a[13] + a[14] * FroudeNoLDep + a[15] * (FroudeNoLDep**2)) + (CB**2) * (a[16] + a[17] * FroudeNoLDep + a[18] * (FroudeNoLDep**2))
    RemainingCoefHol = CR_standard * CR_Fn_krit * kL * (Draught / Beam)**a[0] * ((Beam / LengthPP)**a[1]) * ((LengthDEP / LengthWL)**a[2]) * ((LengthWL / LengthPP)**a[3]) * ((1 + ((DraughtStern - DraughtFore) / LengthPP))**a[4]) * ((D / DraughtStern)**a[5]) * ((1 + NoRudders)**a[6])* ((1 + NoBraces)**a[7]) * ((1 + NoBossings)**a[8]) * ((1 + NoThrusters)**a[9])
    RemainingResHol = RemainingCoefHol * (RoSalt / 2) * SpeedMS**2 * (Beam * Draught / 10)
    return RemainingResHol

RemainingResHol = RemainingResHol(a, LengthPP, CB, FroudeNoLDep, Draught, Beam, LengthDEP, LengthWL, DraughtStern, DraughtFore, D, NoRudders, NoBraces, NoBossings, NoThrusters, RoSalt, SpeedMS)
#print('Remaining resistance by Hollenbach =', RemainingResHol, '[kN]')


def RemainingResHolCruising(a, LengthPP, CB, FroudeNoLDepCruising, Draught, Beam, LengthDEP, LengthWL, DraughtStern, DraughtFore, D, NoRudders, NoBraces, NoBossings, NoThrusters, RoSalt, SpeedCruisingMS):
    kL = a[22] * (LengthPP**a[23])
    FroudeNo_krit = a[19] + (a[20] * CB) + (a[21] * (CB**2))
    CR_Fn_krit_Cruising = np.maximum(1.0, (FroudeNoLDepCruising / FroudeNo_krit)**(FroudeNoLDepCruising / FroudeNo_krit))
    CR_standard_Cruising = a[10] + a[11] * FroudeNoLDepCruising + a[12] * (FroudeNoLDepCruising**2) + CB * (a[13] + a[14] * FroudeNoLDepCruising + a[15] * (FroudeNoLDepCruising**2)) + (CB**2) * (a[16] + a[17] * FroudeNoLDepCruising + a[18] * (FroudeNoLDepCruising**2))
    RemainingCoefHolCruising = CR_standard_Cruising * CR_Fn_krit_Cruising * kL * (Draught / Beam)**a[0] * ((Beam / LengthPP)**a[1]) * ((LengthDEP / LengthWL)**a[2]) * ((LengthWL / LengthPP)**a[3]) * ((1 + ((DraughtStern - DraughtFore) / LengthPP))**a[4]) * ((D / DraughtStern)**a[5]) * ((1 + NoRudders)**a[6])* ((1 + NoBraces)**a[7]) * ((1 + NoBossings)**a[8]) * ((1 + NoThrusters)**a[9])
    RemainingResHolCruising = RemainingCoefHolCruising * (RoSalt / 2) * SpeedCruisingMS**2 * (Beam * Draught / 10)
    return RemainingResHolCruising

RemainingResHolCruising = RemainingResHolCruising(a, LengthPP, CB, FroudeNoLDepCruising, Draught, Beam, LengthDEP, LengthWL, DraughtStern, DraughtFore, D, NoRudders, NoBraces, NoBossings, NoThrusters, RoSalt, SpeedCruisingMS)
#print('Remaining resistance by Hollenbach for cruising speed =', RemainingResHolCruising, '[kN]')


def CorelationResHol(RoSalt, S, SpeedMS, AppendageCoef):
    CorelationResHol = 0.5 * RoSalt * S * SpeedMS**2 * AppendageCoef
    return CorelationResHol

CorelationResHol = CorelationResHol(RoSalt, S, SpeedMS, AppendageCoef)
#print('Corelation resistance by Hollenbach =', CorelationResHol, '[kN]')


def CorelationResHolCruising(RoSalt, S, SpeedCruisingMS, AppendageCoef):
    CorelationResHolCruising = 0.5 * RoSalt * S * SpeedCruisingMS**2 * AppendageCoef
    return CorelationResHolCruising

CorelationResHolCruising = CorelationResHolCruising(RoSalt, S, SpeedCruisingMS, AppendageCoef)
#print('Corelation resistance by Hollenbach for cruising speed =', CorelationResHolCruising, '[kN]')


def TotalResHol(RemainingResHol, FrictionRes, CorelationResHol):
    TotalResHol = RemainingResHol + FrictionRes + CorelationResHol
    return TotalResHol

TotalResHol = TotalResHol(RemainingResHol, FrictionRes, CorelationResHol)
#print('Total resistance by Hollenbach =', TotalResHol, '[kN]')


def TotalResHolCruising(RemainingResHolCruising, FrictionResCruising, CorelationResHolCruising):
    TotalResHolCruising = RemainingResHolCruising + FrictionResCruising + CorelationResHolCruising
    return TotalResHolCruising

TotalResHolCruising = TotalResHolCruising(RemainingResHolCruising, FrictionResCruising, CorelationResHolCruising)
#print('Total resistance by Hollenbach =', TotalResHolCruising, '[kN]')


def EffectivePowerHol(SpeedMS, TotalResHol):
    EffectivePowerHol = SpeedMS * TotalResHol
    return EffectivePowerHol

EffectivePowerHol = EffectivePowerHol(SpeedMS, TotalResHol)
#print('Effective power by GH =', EffectivePowerHol, '[kW]')


def EffectivePowerHolCruising(SpeedCruisingMS, TotalResHolCruising):
    EffectivePowerHolCruising = SpeedCruisingMS * TotalResHolCruising
    return EffectivePowerHolCruising

EffectivePowerHolCruising = EffectivePowerHolCruising(SpeedCruisingMS, TotalResHolCruising)
#print('Effective power at cruising speed by GH =', EffectivePowerHolCruising, '[kW]')


#plt.plot(SpeedMS, CorelationResHol, label = "Corelation Resistance")
#plt.plot(SpeedMS, FrictionRes, label = "Friction Resistance")
#plt.plot(SpeedMS, RemainingResHol, label = "Remaining Resistance")
#plt.plot(SpeedMS, TotalResHol, label = "Total Resistance")
#plt.xticks()
#plt.yticks()
#plt.ylabel("Resistance R [kN]")
#plt.xlabel("Speed V [m/s]")
#plt.grid()
#plt.legend(loc="best")
#plt.show()
