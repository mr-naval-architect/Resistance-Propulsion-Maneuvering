import matplotlib.pyplot as plt
import numpy as np


from Input import LengthWL
from Input import Beam
from Input import Draught
from Input import DraughtFore

from Input import Volume

from Input import CB
from Input import CP
from Input import CM
from Input import CWP
from Input import LCB

from Input import RoSalt
from Input import g

from Input import AppendageCoef
from Input import ABT
from Input import hB
from Input import AT
from Input import CStern

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
# HOLTROP & MENNEN - APPROXIMATE RESISTANCE AND POWER PREDICTION METHOD
# ======================================================================================================================

# Appendage resistance

# This should be completed according to the method in the future
# For now, I will add appandage resistance according to ITTC-57 reccomendation


def AppendageResHM(RoSalt, S, SpeedMS, AppendageCoef):
    AppendageResHM = 0.5 * RoSalt * S * SpeedMS ** 2 * AppendageCoef
    return AppendageResHM

AppendageResHM = AppendageResHM(RoSalt, S, SpeedMS, AppendageCoef)
#print('Appendage resistance by H&M =', AppendageResHM)


def AppendageResHMCruising(RoSalt, S, SpeedCruisingMS, AppendageCoef):
    AppendageResHMCruising = 0.5 * RoSalt * S * SpeedCruisingMS ** 2 * AppendageCoef
    return AppendageResHMCruising

AppendageResHMCruising = AppendageResHMCruising(RoSalt, S, SpeedCruisingMS, AppendageCoef)
#print('Appendage resistance at cruising speed by H&M =', AppendageResHMCruising)


#OnePlusk2eq        equivalation of all appendages

# increase due to the bow thruster tunnel

#AppendageResHM = 0.5 * RoSalt * SpeedMS**2 * SAppendage * OnePlusk2eq


# ======================================================================================================================

# Wave making resistance

def WaveMakingResHM(CP, LCB, LengthWL, Beam, CWP, Volume, ABT, Draught, DraughtFore, hB, FroudeNo, g, RoSalt, AT, CM):
    d = -0.9
    LengthRunHM = (1 - CP + ((0.06 * CP * LCB) / (4 * CP - 1))) * LengthWL
    iEHM = 1 + 89 * np.exp(-((LengthWL / Beam) ** 0.80856) * ((1 - CWP) ** 0.30484) *
                           ((1 - CP - 0.0225 * LCB) ** 0.6367) * ((LengthRunHM / Beam) ** 0.34574) *
                           ((100 * Volume / (LengthWL ** 3)) ** 0.16302))
    if LengthWL / Beam < 12:
        lambdaHM = 1.446 * CP - 0.03 * LengthWL / Beam
    else:
        lambdaHM = 1.446 * CP - 0.36

    if CP < 0.8:
        c16HM = 8.07981 * CP - 13.8673 * (CP ** 2) + 6.984388 * (CP ** 3)
    else:
        c16HM = 1.73014 - 0.7067 * CP

    if (LengthWL ** 3) / Volume < 512:
        c15HM = -1.69385
    elif 512 <= (LengthWL ** 3) / Volume < 1727:
        c15HM = - 1.69385 + (LengthWL / (Volume ** (1 / 3)) - 8) / 2.36
    else:
        c15HM = 0

    if Beam / LengthWL <= 0.11:
        c7HM = 0.229577 * (Beam / LengthWL) ** 0.33333
    elif 0.11 < Beam / LengthWL <= 0.25:
        c7HM = Beam / LengthWL
    else:
        c7HM = 0.5 - 0.0625 * LengthWL / Beam

    c5HM = 1 - (0.8 * AT) / (Beam * Draught * CM)

    c3HM = (0.56 * (ABT ** 1.5)) / (Beam * Draught * (0.31 * np.sqrt(ABT) + DraughtFore - hB))

    c2HM = np.exp(-1.89 * np.sqrt(c3HM))

    c1HM = 2223105 * (c7HM ** 3.78613) * ((Draught / Beam) ** 1.07961) * ((90 - iEHM) ** (-1.37565))

    m2HM = c15HM * (CP ** 2) * np.exp(-0.1 * (FroudeNo ** (-2)))  # This is the only value here that is an array

    m1HM = 0.0140407 * LengthWL / Beam - 1.75254 * (Volume ** (1 / 3)) / LengthWL - 4.79323 * Beam / LengthWL - c16HM

    WaveMakingResHM = c1HM * c2HM * c5HM * Volume * RoSalt * g * np.exp(m1HM * FroudeNo ** d + m2HM * np.cos(lambdaHM *
                                                                                                             FroudeNo ** (
                                                                                                                 -2)))
    return WaveMakingResHM

WaveMakingResHM = WaveMakingResHM(CP, LCB, LengthWL, Beam, CWP, Volume, ABT, Draught, DraughtFore, hB, FroudeNo, g, RoSalt, AT, CM)
#print('WaveMakingResHM is:', WaveMakingResHM)


def WaveMakingResHMCruising(CP, LCB, LengthWL, Beam, CWP, Volume, ABT, Draught, DraughtFore, hB, FroudeNoCruising, g,
                            RoSalt, AT, CM):
    d = -0.9
    LengthRunHM = (1 - CP + ((0.06 * CP * LCB) / (4 * CP - 1))) * LengthWL
    iEHM = 1 + 89 * np.exp(-((LengthWL / Beam) ** 0.80856) * ((1 - CWP) ** 0.30484) *
                           ((1 - CP - 0.0225 * LCB) ** 0.6367) * ((LengthRunHM / Beam) ** 0.34574) *
                           ((100 * Volume / (LengthWL ** 3)) ** 0.16302))
    if LengthWL / Beam < 12:
        lambdaHM = 1.446 * CP - 0.03 * LengthWL / Beam
    else:
        lambdaHM = 1.446 * CP - 0.36

    if CP < 0.8:
        c16HM = 8.07981 * CP - 13.8673 * (CP ** 2) + 6.984388 * (CP ** 3)
    else:
        c16HM = 1.73014 - 0.7067 * CP

    if (LengthWL ** 3) / Volume < 512:
        c15HM = -1.69385
    elif 512 <= (LengthWL ** 3) / Volume < 1727:
        c15HM = - 1.69385 + (LengthWL / (Volume ** (1 / 3)) - 8) / 2.36
    else:
        c15HM = 0

    if Beam / LengthWL <= 0.11:
        c7HM = 0.229577 * (Beam / LengthWL) ** 0.33333
    elif 0.11 < Beam / LengthWL <= 0.25:
        c7HM = Beam / LengthWL
    else:
        c7HM = 0.5 - 0.0625 * LengthWL / Beam

    c5HM = 1 - (0.8 * AT) / (Beam * Draught * CM)

    c3HM = (0.56 * (ABT ** 1.5)) / (Beam * Draught * (0.31 * np.sqrt(ABT) + DraughtFore - hB))

    c2HM = np.exp(-1.89 * np.sqrt(c3HM))

    c1HM = 2223105 * (c7HM ** 3.78613) * ((Draught / Beam) ** 1.07961) * ((90 - iEHM) ** (-1.37565))

    m2HM = c15HM * (CP ** 2) * np.exp(-0.1 * (FroudeNoCruising ** (-2)))  # This is the only value here that is an array

    m1HM = 0.0140407 * LengthWL / Beam - 1.75254 * (Volume ** (1 / 3)) / LengthWL - 4.79323 * Beam / LengthWL - c16HM

    WaveMakingResHMCruising = c1HM * c2HM * c5HM * Volume * RoSalt * g * np.exp(m1HM * FroudeNoCruising ** d + m2HM * np.cos(lambdaHM *
                                                                                                             FroudeNoCruising ** (
                                                                                                                 -2)))
    return WaveMakingResHMCruising

WaveMakingResHMCruising = WaveMakingResHMCruising(CP, LCB, LengthWL, Beam, CWP, Volume, ABT, Draught, DraughtFore, hB, FroudeNoCruising, g, RoSalt, AT, CM)
#print('WaveMakingResHMCruising is:', WaveMakingResHMCruising)


# ======================================================================================================================

# Additional resistance due to bulbous bow near the surface
# There should be an option at the begining to define weather there is a bulb, but ill use ABT for now

def BulbResHM(ABT, SpeedMS, g, DraughtFore, hB, RoSalt):
    if ABT < 0.001:
        BulbResHM = 0 * SpeedMS
    else:
        FroudeNoiHM = SpeedMS / np.sqrt(g * (DraughtFore - hB - 0.25 * np.sqrt(ABT)) + 0.15 * (SpeedMS ** 2))
        PBHM = 0.56 * np.sqrt(ABT) / (DraughtFore - 1.5 * hB)
        BulbResHM = (0.11 * np.exp((-3) / PBHM ** 2) * (FroudeNoiHM ** 3) * (ABT ** 1.5) * RoSalt * g) / (1 + (
                FroudeNoiHM ** 2))
    return BulbResHM

BulbResHM = BulbResHM(ABT, SpeedMS, g, DraughtFore, hB, RoSalt)
#print('BulbResHM is:', BulbResHM)


def BulbResHMCruising(ABT, SpeedCruisingMS, g, DraughtFore, hB, RoSalt):
    if ABT < 0.001:
        BulbResHM = 0 * SpeedCruisingMS
    else:
        FroudeNoiHMCruising = SpeedCruisingMS / np.sqrt(g * (DraughtFore - hB - 0.25 * np.sqrt(ABT)) + 0.15 * (SpeedMS ** 2))
        PBHM = 0.56 * np.sqrt(ABT) / (DraughtFore - 1.5 * hB)
        BulbResHM = (0.11 * np.exp((-3) / PBHM ** 2) * (FroudeNoiHMCruising ** 3) * (ABT ** 1.5) * RoSalt * g) / (1 + (
                FroudeNoiHMCruising ** 2))
    return BulbResHM

BulbResHMCruising = BulbResHMCruising(ABT, SpeedCruisingMS, g, DraughtFore, hB, RoSalt)
#print('BulbResHMCruising is:', BulbResHMCruising)


# ======================================================================================================================

# Additional resistance due to immersed transom

def TransomResHM(SpeedMS, g, AT, Beam, CWP, RoSalt):
    FroudeNoTHM = SpeedMS / np.sqrt(2 * g * AT / (Beam + Beam * CWP))

    c6HM = 0.2 * (1 - 0.2 * FroudeNoTHM)

    for i in range(len(FroudeNoTHM)):
        if FroudeNoTHM[i] >= 5:
            c6HM[i] = 0.0

    TransomResHM = 0.5 * RoSalt * SpeedMS ** 2 * AT * c6HM
    return TransomResHM

TransomResHM = TransomResHM(SpeedMS, g, AT, Beam, CWP, RoSalt)
#print('transom resistance is:', TransomResHM)


def TransomResHMCruising(SpeedCruisingMS, g, AT, Beam, CWP, RoSalt):
    FroudeNoTHMCruising = SpeedCruisingMS / np.sqrt(2 * g * AT / (Beam + Beam * CWP))

    c6HM = 0.2 * (1 - 0.2 * FroudeNoTHMCruising)

    if FroudeNoTHMCruising >= 5:
        c6HM = 0.0

    TransomResHMCruising = 0.5 * RoSalt * SpeedCruisingMS ** 2 * AT * c6HM
    return TransomResHMCruising

TransomResHMCruising = TransomResHMCruising(SpeedCruisingMS, g, AT, Beam, CWP, RoSalt)
#print('transom resistance for cruising speed is:', TransomResHMCruising)


# ======================================================================================================================

# Resistance due to model - ship correlation

def CorelationResHM(ABT, Beam, Draught, DraughtFore, hB, LengthWL, CB, RoSalt, SpeedMS):
    c3HM = (0.56 * (ABT ** 1.5)) / (Beam * Draught * (0.31 * np.sqrt(ABT) + DraughtFore - hB))

    c2HM = np.exp(-1.89 * np.sqrt(c3HM))

    if DraughtFore / LengthWL <= 0.04:
        c4HM = DraughtFore / LengthWL
    else:
        c4HM = 0.04

    CAHM = 0.006 * ((LengthWL + 100) ** (-0.16)) - 0.00205 + 0.003 * np.sqrt(LengthWL / 7.5) * (CB ** 4) * c2HM * (
                0.04 - c4HM)

    CorelationResHM = 0.5 * RoSalt * SpeedMS ** 2 * S * CAHM
    return CorelationResHM

CorelationResHM = CorelationResHM(ABT, Beam, Draught, DraughtFore, hB, LengthWL, CB, RoSalt, SpeedMS)
#print('CorelationResHM is:', CorelationResHM)


def CorelationResHMCruising(ABT, Beam, Draught, DraughtFore, hB, LengthWL, CB, RoSalt, SpeedCruisingMS):
    c3HM = (0.56 * (ABT ** 1.5)) / (Beam * Draught * (0.31 * np.sqrt(ABT) + DraughtFore - hB))

    c2HM = np.exp(-1.89 * np.sqrt(c3HM))

    if DraughtFore / LengthWL <= 0.04:
        c4HM = DraughtFore / LengthWL
    else:
        c4HM = 0.04

    CAHM = 0.006 * ((LengthWL + 100) ** (-0.16)) - 0.00205 + 0.003 * np.sqrt(LengthWL / 7.5) * (CB ** 4) * c2HM * (
                0.04 - c4HM)

    CorelationResHMCruising = 0.5 * RoSalt * SpeedCruisingMS ** 2 * S * CAHM
    return CorelationResHMCruising

CorelationResHMCruising = CorelationResHMCruising(ABT, Beam, Draught, DraughtFore, hB, LengthWL, CB, RoSalt, SpeedCruisingMS)
#print('CorelationResHMCruising is:', CorelationResHMCruising)


# ======================================================================================================================

# Total ship resistance

def TotalResHM(CP, LCB, LengthWL, Draught, CStern, Beam, FrictionRes, AppendageResHM, WaveMakingResHM, BulbResHM,
               TransomResHM, CorelationResHM):
    LengthRunHM = (1 - CP + ((0.06 * CP * LCB) / (4 * CP - 1))) * LengthWL

    if Draught / LengthWL >= 0.05:
        c12HM = (Draught / LengthWL) ** 0.2228446
    elif 0.02 <= Draught / LengthWL < 0.05:
        c12HM = 48.2 * ((Draught / LengthWL - 0.02) ** 2.078) + 0.479948
    else:
        c12HM = 0.479948

    c13HM = 1 + 0.003 * CStern

    k1HM = c13HM * (0.93 + c12HM * ((Beam / LengthRunHM) ** 0.92497) * ((0.95 - CP) ** (-0.521448)) * (
                (1 - CP + 0.0225 * LCB
                 ) ** 0.6906)) - 1

    TotalResHM = FrictionRes * (
                1 + k1HM) + AppendageResHM + WaveMakingResHM + BulbResHM + TransomResHM + CorelationResHM
    return TotalResHM

TotalResHM = TotalResHM(CP, LCB, LengthWL, Draught, CStern, Beam, FrictionRes, AppendageResHM, WaveMakingResHM, BulbResHM,
               TransomResHM, CorelationResHM)
#print('Resistance by HM =', TotalResHM, '[kN]')


def TotalResHMCruising(CP, LCB, LengthWL, Draught, CStern, Beam, FrictionResCruising, AppendageResHMCruising,
                       WaveMakingResHMCruising,
                       BulbResHMCruising,
               TransomResHMCruising, CorelationResHMCruising):
    LengthRunHM = (1 - CP + ((0.06 * CP * LCB) / (4 * CP - 1))) * LengthWL

    if Draught / LengthWL >= 0.05:
        c12HM = (Draught / LengthWL) ** 0.2228446
    elif 0.02 <= Draught / LengthWL < 0.05:
        c12HM = 48.2 * ((Draught / LengthWL - 0.02) ** 2.078) + 0.479948
    else:
        c12HM = 0.479948

    c13HM = 1 + 0.003 * CStern

    k1HM = c13HM * (0.93 + c12HM * ((Beam / LengthRunHM) ** 0.92497) * ((0.95 - CP) ** (-0.521448)) * (
                (1 - CP + 0.0225 * LCB
                 ) ** 0.6906)) - 1

    TotalResHMCruising = FrictionResCruising * (
                1 + k1HM) + AppendageResHMCruising + WaveMakingResHMCruising + BulbResHMCruising + TransomResHMCruising + CorelationResHMCruising
    return TotalResHMCruising

TotalResHMCruising = TotalResHMCruising(CP, LCB, LengthWL, Draught, CStern, Beam, FrictionResCruising, AppendageResHMCruising,
                       WaveMakingResHMCruising,
                       BulbResHMCruising,
               TransomResHMCruising, CorelationResHMCruising)
#print('Resistance at cruising speed by HM =', TotalResHMCruising, '[kN]')
#print('')


def EffectivePowerHM(SpeedMS, TotalResHM):
    EffectivePowerHM = SpeedMS * TotalResHM
    return EffectivePowerHM

EffectivePowerHM = EffectivePowerHM(SpeedMS, TotalResHM)
#print('Effective power by HM =', EffectivePowerHM, '[kW]')


def EffectivePowerHMCruising(SpeedCruisingMS, TotalResHMCruising):
    EffectivePowerHMCruising = SpeedCruisingMS * TotalResHMCruising
    return EffectivePowerHMCruising

EffectivePowerHMCruising = EffectivePowerHMCruising(SpeedCruisingMS, TotalResHMCruising)
#print('Effective power at cruising speed by HM =', EffectivePowerHMCruising, '[kW]')
#print('')


#plt.plot(SpeedMS, AppendageResHM, label = "Appendage Resistance")
#plt.plot(SpeedMS, WaveMakingResHM, label = "Wawe Making Resistance")
#plt.plot(SpeedMS, BulbResHM, label = "Bulb Resistance")
#plt.plot(SpeedMS, TransomResHM, label = "Transom Resistance")
#plt.plot(SpeedMS, CorelationResHM, label = "Corelation Resistance")
#plt.plot(SpeedMS, TotalResHM, label = "Total Resistance")
#plt.xticks()
#plt.yticks()
#plt.ylabel("Resistance R [kN]")
#plt.xlabel("Speed V [m/s]")
#plt.grid()
#plt.legend(loc="best")
#plt.show()



