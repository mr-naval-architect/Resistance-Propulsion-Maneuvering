import matplotlib.pyplot as plt
import numpy as np


from Input import LengthDEP
from Input import Beam
from Input import Draught

from Input import Volume

from Input import CP
from Input import LCB

from Input import RoSalt

from Input import AppendageCoef

from Input import SpeedMS
from Input import SpeedCruisingMS

from Input import FroudeNoLDep
from Input import FroudeNoLDepCruising

from Wetted_Surface import S

from Friction_Res import FrictionCoef
from Friction_Res import FrictionCoefCruising


# ======================================================================================================================
# GULDHAMMER - HARVALD - APPROXIMATE RESISTANCE AND POWER PREDICTION METHOD
# ======================================================================================================================

# 1. Base coefficient
# The result of the following calculation gives the base value multiplied by 1000
# This value is later modified by various corrective coefficients

def RemainingBaseCoef1000GH(LengthDEP, Volume, CP, FroudeNoLDep):
    M_GH = LengthDEP / (Volume ** (1 / 3))
    A0_GH = 1.35 - 0.23 * M_GH + 0.012 * M_GH ** 2
    A1_GH = 0.0011 * M_GH ** 9.1
    N1_GH = 2 * M_GH - 3.7
    E_GH = (A0_GH + 1.5 * FroudeNoLDep ** 1.8 + A1_GH * FroudeNoLDep ** N1_GH) * (0.98 + 2.5 / (M_GH - 2) ** 4) + (
                M_GH - 5) ** 4 * (FroudeNoLDep - 0.1) ** 4
    B1_GH = 7 - 0.09 * M_GH ** 2
    B2_GH = (5 * CP - 2.5) ** 2
    B3_GH = (600 * (FroudeNoLDep - 0.315) ** 2 + 1) ** 1.5
    G_GH = (B1_GH * B2_GH) / B3_GH
    H_GH = np.exp(80 * (FroudeNoLDep - (0.04 + 0.59 * CP) - 0.015 * (M_GH - 5)))
    K_GH = 180 * (FroudeNoLDep ** 3.7) * np.exp(20 * CP - 16)
    RemainingBaseCoef1000GH = E_GH + G_GH + H_GH + K_GH
    return RemainingBaseCoef1000GH

RemainingBaseCoef1000GH = RemainingBaseCoef1000GH(LengthDEP, Volume, CP, FroudeNoLDep)
#print('Base coefficient of remaining resistance multiplied by 1000 by GH is:', RemainingBaseCoef1000GH)


def RemainingBaseCoef1000GHCruising(LengthDEP, Volume, CP, FroudeNoLDepCruising):
    M_GH = LengthDEP / (Volume ** (1 / 3))
    A0_GH = 1.35 - 0.23 * M_GH + 0.012 * M_GH ** 2
    A1_GH = 0.0011 * M_GH ** 9.1
    N1_GH = 2 * M_GH - 3.7
    E_GH = (A0_GH + 1.5 * FroudeNoLDepCruising ** 1.8 + A1_GH * FroudeNoLDepCruising ** N1_GH) * (0.98 + 2.5 / (M_GH - 2) ** 4) + (
                M_GH - 5) ** 4 * (FroudeNoLDepCruising - 0.1) ** 4
    B1_GH = 7 - 0.09 * M_GH ** 2
    B2_GH = (5 * CP - 2.5) ** 2
    B3_GH = (600 * (FroudeNoLDepCruising - 0.315) ** 2 + 1) ** 1.5
    G_GH = (B1_GH * B2_GH) / B3_GH
    H_GH = np.exp(80 * (FroudeNoLDepCruising - (0.04 + 0.59 * CP) - 0.015 * (M_GH - 5)))
    K_GH = 180 * (FroudeNoLDepCruising ** 3.7) * np.exp(20 * CP - 16)
    RemainingBaseCoef1000GHCruising = E_GH + G_GH + H_GH + K_GH
    return RemainingBaseCoef1000GHCruising

RemainingBaseCoef1000GHCruising = RemainingBaseCoef1000GHCruising(LengthDEP, Volume, CP, FroudeNoLDepCruising)
#print('Base coefficient of remaining resistance multiplied by 1000 by GH for cruising speed is:',
#      RemainingBaseCoef1000GHCruising)


# ======================================================================================================================

# 2. Corrective coefficient based on Beam/Draught

def CoefBeamDraught1000GH(Beam, Draught):
    if Beam / Draught == 2.5:
        CoefBeamDraught1000GH = 0
    else:
        CoefBeamDraught1000GH = 0.16 * (Beam / Draught - 2.5)
    return CoefBeamDraught1000GH

CoefBeamDraught1000GH = CoefBeamDraught1000GH(Beam, Draught)
#print('CR B/T * 1000 =', CoefBeamDraught1000GH)

CoefBeamDraught1000GHCruising = CoefBeamDraught1000GH


# ======================================================================================================================

# 3. Corrective coefficient based on LCB

# Next calculation consists of two brackets. Both of these need to be a positive number.
# If both brackets are not a positive number, The coefficient is 0

def CoefLCB1000GH(FroudeNoLDep, LengthDEP, CP, LCB):
    LCB_StandardGH = (0.44 * FroudeNoLDep - 0.094) * LengthDEP

    CoefLCB1000GHBracket1 = (FroudeNoLDep / (CP ** 2 + 1.1 * CP - 0.0875)) - 1
    CoefLCB1000GHBracket2 = (LCB_StandardGH / LengthDEP) - (LCB / LengthDEP)

    for i in range(len(CoefLCB1000GHBracket1)):
        if CoefLCB1000GHBracket1[i] < 0:
            CoefLCB1000GHBracket1[i] = 0

    for i in range(len(CoefLCB1000GHBracket2)):
        if CoefLCB1000GHBracket2[i] < 0:
            CoefLCB1000GHBracket2[i] = 0

    CoefLCB1000GH = 90 * CoefLCB1000GHBracket1 * CoefLCB1000GHBracket2
    return CoefLCB1000GH

CoefLCB1000GH = CoefLCB1000GH(FroudeNoLDep, LengthDEP, CP, LCB)
#print('CoefLCB1000GH:', CoefLCB1000GH)


def CoefLCB1000GHCruising(FroudeNoLDepCruising, LengthDEP, CP, LCB):
    LCB_StandardGH = (0.44 * FroudeNoLDepCruising - 0.094) * LengthDEP

    CoefLCB1000GHBracket1 = (FroudeNoLDepCruising / (CP ** 2 + 1.1 * CP - 0.0875)) - 1
    CoefLCB1000GHBracket2 = (LCB_StandardGH / LengthDEP) - (LCB / LengthDEP)

    if CoefLCB1000GHBracket1 < 0:
        CoefLCB1000GHBracket1 = 0

    if CoefLCB1000GHBracket2 < 0:
        CoefLCB1000GHBracket2 = 0

    CoefLCB1000GHCruising = 90 * CoefLCB1000GHBracket1 * CoefLCB1000GHBracket2
    return CoefLCB1000GHCruising

CoefLCB1000GHCruising = CoefLCB1000GHCruising(FroudeNoLDepCruising, LengthDEP, CP, LCB)
#print('CoefLCB1000GHCruising:', CoefLCB1000GHCruising)


# ======================================================================================================================

# 4. Corrective coefficient based on the shape of ribs
# To be done in the future

CoefRib1000GH = 0

CoefRib1000GHCruising = 0


# ======================================================================================================================

# 5. Corrective coefficient based on the bulb
# To be done in the future

CoefBulb1000GH = 0

CoefBulb1000GHCruising = 0


# ======================================================================================================================

# 6. Corrective coefficient for the appandages
# To be done in the future

CoefApp1000GH = 0

CoefApp1000GHCruising = 0


# ======================================================================================================================

# 7. corrective coefficient for wind and manouevaring
# To be done in the future

CoefWM1000GH = 0

CoefWM1000GHCruising = 0


# ======================================================================================================================

# Following calculation gives the correct value of the remaining resistance coefficient and remaining resistance force.

def RemainingCoefGH(RemainingBaseCoef1000GH, CoefBeamDraught1000GH, CoefLCB1000GH, CoefRib1000GH, CoefBulb1000GH,
                    CoefApp1000GH, CoefWM1000GH):
    RemainingCoefGH = (RemainingBaseCoef1000GH + CoefBeamDraught1000GH + CoefLCB1000GH + CoefRib1000GH +
                       CoefBulb1000GH + CoefApp1000GH + CoefWM1000GH) / 1000
    return RemainingCoefGH

RemainingCoefGH = RemainingCoefGH(RemainingBaseCoef1000GH, CoefBeamDraught1000GH, CoefLCB1000GH, CoefRib1000GH, CoefBulb1000GH,
                    CoefApp1000GH, CoefWM1000GH)


def RemainingCoefGHCruising(RemainingBaseCoef1000GHCruising, CoefBeamDraught1000GHCruising, CoefLCB1000GHCruising,
                            CoefRib1000GHCruising, CoefBulb1000GHCruising, CoefApp1000GHCruising, CoefWM1000GHCruising):
    RemainingCoefGHCruising = (RemainingBaseCoef1000GHCruising + CoefBeamDraught1000GHCruising + CoefLCB1000GHCruising
                              + CoefRib1000GHCruising + CoefBulb1000GHCruising + CoefApp1000GHCruising +
                               CoefWM1000GHCruising) / 1000
    return RemainingCoefGHCruising

RemainingCoefGHCruising = RemainingCoefGHCruising(RemainingBaseCoef1000GHCruising, CoefBeamDraught1000GHCruising,
                                                  CoefLCB1000GHCruising,CoefRib1000GHCruising, CoefBulb1000GHCruising,
                                                  CoefApp1000GHCruising, CoefWM1000GHCruising)


def RemainingResGH(RoSalt, S, SpeedMS, RemainingCoefGH):
    RemainingResGH = 0.5 * RoSalt * S * SpeedMS ** 2 * RemainingCoefGH
    return RemainingResGH

RemainingResGH = RemainingResGH(RoSalt, S, SpeedMS, RemainingCoefGH)
#print('Remaining resistance by GH =', RemainingResGH, '[kN]')


def RemainingResGHCruising(RoSalt, S, SpeedCruisingMS, RemainingCoefGHCruising):
    RemainingResGHCruising = 0.5 * RoSalt * S * SpeedCruisingMS ** 2 * RemainingCoefGHCruising
    return RemainingResGHCruising

RemainingResGHCruising = RemainingResGHCruising(RoSalt, S, SpeedCruisingMS, RemainingCoefGHCruising)
#print('Remaining resistance for cruising speed by GH =', RemainingResGHCruising, '[kN]')


def TotalCoefGH(FrictionCoef, RemainingCoefGH, AppendageCoef):
    TotalCoefGH = FrictionCoef + RemainingCoefGH + AppendageCoef
    return TotalCoefGH

TotalCoefGH = TotalCoefGH(FrictionCoef, RemainingCoefGH, AppendageCoef)


def TotalCoefGHCruising(FrictionCoefCruising, RemainingCoefGHCruising, AppendageCoef):
    TotalCoefGHCruising = FrictionCoefCruising + RemainingCoefGHCruising + AppendageCoef
    return TotalCoefGHCruising

TotalCoefGHCruising = TotalCoefGHCruising(FrictionCoefCruising, RemainingCoefGHCruising, AppendageCoef)


def TotalResGH(RoSalt, S, SpeedMS, TotalCoefGH):
    TotalResGH = 0.5 * RoSalt * S * SpeedMS ** 2 * TotalCoefGH
    return TotalResGH

TotalResGH = TotalResGH(RoSalt, S, SpeedMS, TotalCoefGH)
#print('Resistance by GH =', TotalResGH, '[kN]')


def TotalResGHCruising(RoSalt, S, SpeedCruisingMS, TotalCoefGHCruising):
    TotalResGHCruising = 0.5 * RoSalt * S * SpeedCruisingMS ** 2 * TotalCoefGHCruising
    return TotalResGHCruising

TotalResGHCruising = TotalResGHCruising(RoSalt, S, SpeedCruisingMS, TotalCoefGHCruising)
#print('Resistance at cruising speed by GH =', TotalResGHCruising, '[kN]')
#print('')

def EffectivePowerGH(SpeedMS, TotalResGH):
    EffectivePowerGH = SpeedMS * TotalResGH
    return EffectivePowerGH

EffectivePowerGH = EffectivePowerGH(SpeedMS, TotalResGH)
#print('Effective power by GH =', EffectivePowerGH, '[kW]')


def EffectivePowerGHCruising(SpeedCruisingMS, TotalResGHCruising):
    EffectivePowerGHCruising = SpeedCruisingMS * TotalResGHCruising
    return EffectivePowerGHCruising

EffectivePowerGHCruising = EffectivePowerGHCruising(SpeedCruisingMS, TotalResGHCruising)
#print('Effective power at cruising speed by GH =', EffectivePowerGHCruising, '[kW]')
#print('')

#plt.plot(SpeedMS, FrictionRes)
#plt.plot(SpeedMS, RemainingResGH)
#plt.plot(SpeedMS, TotalResGH)
#plt.xticks()
#plt.yticks()
#plt.ylabel("Resistance R [kN]")
#plt.xlabel("Speed V [m/s]")
#plt.grid()
#plt.show()

