import matplotlib.pyplot as plt
import numpy as np


from Input import LengthWL
from Input import Beam
from Input import Draught
from Input import DraughtFore
from Input import DraughtStern

from Input import CB
from Input import CP
from Input import LCB

from Input import D
from Input import ABT
from Input import hB
from Input import CStern
from Input import NoPropellers

from Input import SpeedCruisingMS

from Input import MaxDeviation_w
from Input import MaxDeviation_t

from Wetted_Surface import S

from Friction_Res import FrictionCoefCruising

from GH_Res import EffectivePowerGHCruising
from HM_Res import EffectivePowerHMCruising




# ======================================================================================================================
# APPROXIMATE METHODS OF CALCULATION OF WAKE FRACTION
# ======================================================================================================================

# Holtrop & Mennen
# Calculating wake fraction for single screw ships

def w_HM(CP, LCB, LengthWL, Draught, CStern, Beam, ABT, hB, DraughtFore, CB, FrictionCoefCruising, DraughtStern, S,
         D):
    LengthRunHM = (1 - CP + ((0.06 * CP * LCB) / (4 * CP - 1))) * LengthWL

    if Draught / LengthWL >= 0.05:
        c12HM = (Draught / LengthWL) ** 0.2228446
    elif 0.02 <= Draught / LengthWL < 0.05:
        c12HM = 48.2 * ((Draught / LengthWL - 0.02) ** 2.078) + 0.479948
    else:
        c12HM = 0.479948

    c13HM = 1 + 0.003 * CStern

    k1HM = c13HM * (
                0.93 + c12HM * ((Beam / LengthRunHM) ** 0.92497) * ((0.95 - CP) ** (-0.521448)) * ((1 - CP + 0.0225 *
                                                                                                    LCB) ** 0.6906)) - 1

    c3HM = (0.56 * (ABT ** 1.5)) / (Beam * Draught * (0.31 * np.sqrt(ABT) + DraughtFore - hB))

    c2HM = np.exp(-1.89 * np.sqrt(c3HM))

    if DraughtFore / LengthWL <= 0.04:
        c4HM = DraughtFore / LengthWL
    else:
        c4HM = 0.04

    CAHM = 0.006 * ((LengthWL + 100) ** (-0.16)) - 0.00205 + 0.003 * np.sqrt(LengthWL / 7.5) * (CB ** 4) * c2HM * (
                0.04 -
                c4HM)

    CP1HM = 1.45 * CP - 0.315 - 0.0225 * LCB

    CVHM = (1 + k1HM) * FrictionCoefCruising + CAHM

    if Beam / DraughtStern < 5:
        c8HM = Beam * S / (LengthWL * D * DraughtStern)
    else:
        c8HM = S * ((7 * Beam / DraughtStern) - 25) / (LengthWL * D * (Beam / DraughtStern - 3))

    if c8HM < 28:
        c9HM = c8HM
    else:
        c9HM = 32 - 16 / (c8HM - 24)

    if DraughtStern / D < 2:
        c11HM = DraughtStern / D
    else:
        c11HM = 0.0833333 * ((DraughtStern / D) ** 3) + 1.33333

    w_HM = c9HM * CVHM * (LengthWL / DraughtStern) * (0.0661875 + 1.21759 * c11HM * (CVHM / (1 - CP1HM))) + 0.24558 * \
           np.sqrt(Beam / (LengthWL * (1 - CP1HM))) - (0.09726 / (0.95 - CP)) + (
                       0.11434 / (0.95 - CB)) + 0.75 * CStern * \
           CVHM + 0.002 * CStern
    return w_HM

w_HM = w_HM(CP, LCB, LengthWL, Draught, CStern, Beam, ABT, hB, DraughtFore, CB, FrictionCoefCruising, DraughtStern, S,
         D)
#print('w by Holtrop and Mennen is:', w_HM)


# ======================================================================================================================

# Holtrop & Mennen Revised (I will do this in the future)


#CVHMR =

#CP1HMR =

#C9HMR =

#C11HMR =

#C19HMR =

#C20HMR =


#w_HMR = C9HMR * C20HMR * CVHMR * (LengthWL / DraughtStern) * (0.050776 + 0.93405 * C11HMR * (CVHMR / (1 - CP1HMR))) +\
#        0.27915 * C20HMR * np.sqrt(Beam/(LengthWL * ( 1 - CP1HMR))) + C19HMR * C20HMR

w_HMR = 0.0
#print('w by Holtrop and Mennen Revised is:', w_HMR)


# ======================================================================================================================

# Taylor 1910

def w_Taylor1910(CB):
    w_Taylor1910 = 0.5 * CB - 0.05
    return w_Taylor1910

w_Taylor1910 = w_Taylor1910(CB)
#print('w by Taylor 1910 is:', w_Taylor1910)


# ======================================================================================================================

# Taylor 1923

def w_Taylor1923(CB):
    w_Taylor1923 = 0.5 * CB - 0.1
    return w_Taylor1923

w_Taylor1923 = w_Taylor1923(CB)
#print('w by Taylor 1923 is:', w_Taylor1923)


# ======================================================================================================================

# Robertson

def w_Robertson(CP):
    w_Robertson = 0.45 * CP - 0.05
    return w_Robertson

w_Robertson = w_Robertson(CP)
#print('w by Robertson is:', w_Robertson)


# ======================================================================================================================

# Schiffbaukalender

def w_Schiffbaukalender(CB):
    w_Schiffbaukalender = 0.75 * CB - 0.24
    return w_Schiffbaukalender

w_Schiffbaukalender = w_Schiffbaukalender(CB)
#print('w by Schiffbaukalender is:', w_Schiffbaukalender)


# ======================================================================================================================

# Shipbuilding and Shipping Record

def w_SaSR(CP):
    w_SaSR = (CP ** 3) / (1 + (CP ** 3))
    return w_SaSR

w_SaSR = w_SaSR(CP)
#print('w by Shipbuilding and Shipping Record is:', w_SaSR)


# ======================================================================================================================

# Gill

def w_Gill(CB):
    w_Gill = 0.67 * CB - 0.15
    return w_Gill

w_Gill = w_Gill(CB)
#print('w by Gill is:', w_Gill)


# ======================================================================================================================
# AVERAGE VALUE OF THE WAKE FRACTION CALCULATED BY APROXIMATE METHODS
# ======================================================================================================================

# Average of the wake fraction calculated in the section above
# In future versions the user should be able to override this value
# In the future, there should be an option to exclude (manualy and automaticly) values that dont fit

def WakeFraction (w_HM, w_HMR, w_Taylor1910, w_Taylor1923, w_Robertson, w_Schiffbaukalender, w_SaSR, w_Gill):

    w_check = (w_HM + w_HMR + w_Taylor1910 + w_Taylor1923 + w_Robertson + w_Schiffbaukalender + w_SaSR + w_Gill) / 8

    Numerator_w = 0

    Denominator_w = 0

    DeviationComparator_w = MaxDeviation_w * w_check
    if abs(w_HM - w_check) <= DeviationComparator_w:
        Numerator_w += w_HM
        Denominator_w += 1

    if abs(w_HMR - w_check) <= DeviationComparator_w:
        Numerator_w += w_HMR
        Denominator_w += 1

    if abs(w_Taylor1910 - w_check) <= DeviationComparator_w:
        Numerator_w += w_Taylor1910
        Denominator_w += 1

    if abs(w_Taylor1923 - w_check) <= DeviationComparator_w:
        Numerator_w += w_Taylor1923
        Denominator_w += 1

    if abs(w_Robertson - w_check) <= DeviationComparator_w:
        Numerator_w += w_Robertson
        Denominator_w += 1

    if abs(w_Schiffbaukalender - w_check) <= DeviationComparator_w:
        Numerator_w += w_Schiffbaukalender
        Denominator_w += 1

    if abs(w_SaSR - w_check) <= DeviationComparator_w:
        Numerator_w += w_SaSR
        Denominator_w += 1

    if abs(w_Gill - w_check) <= DeviationComparator_w:
        Numerator_w += w_Gill
        Denominator_w += 1

    w = Numerator_w / Denominator_w
    return w

w = WakeFraction (w_HM, w_HMR, w_Taylor1910, w_Taylor1923, w_Robertson, w_Schiffbaukalender, w_SaSR, w_Gill)
#print('The average value of wake fraction is w =', w)
#print('')

# ======================================================================================================================
# CALCULATING THE SPEED OF ADVANCE
# ======================================================================================================================

AdvanceSpeedMS = SpeedCruisingMS * (1 - w)
#print('Speed of advance VA =', AdvanceSpeedMS, '[m/s]')
#print('')


# ======================================================================================================================
# APPROXIMATE METHODS OF CALCULATION OF THRUST DEDUCTION
# ======================================================================================================================

# Holtrop & Mennen
# Calculating thrust deduction for single screw ships

def t_HM(CP, LCB, LengthWL, Beam, D, Draught, CStern):
    CP1HM = 1.45 * CP - 0.315 - 0.0225 * LCB

    if LengthWL / Beam > 5.2:
        c10HM = Beam / LengthWL
    else:
        c10HM = 0.25 - (0.003328402 / ((Beam / LengthWL) - 0.134615385))

    t_HM = 0.001979 * (LengthWL / (Beam - Beam * CP1HM)) + 1.0585 * c10HM - 0.00524 - \
           ((0.1418 * (D ** 2)) / (Beam * Draught)) + 0.0015 * CStern
    return t_HM

t_HM = t_HM(CP, LCB, LengthWL, Beam, D, Draught, CStern)
#print('t by Holtrop and Mennen is:', t_HM)


# ======================================================================================================================

# Holtrop & Mennen Revised (I will do this in the future)

t_HMR = t_HM
#print('t by Holtrop and Mennen revised is:', t_HMR)


# ======================================================================================================================

# Taylor 1923

def t_Taylor1923(CB):
    t_Taylor1923 = 0.3 * CB
    return t_Taylor1923

t_Taylor1923 = t_Taylor1923(CB)
#print('t by Taylor 1923 is:', t_Taylor1923)


# ======================================================================================================================

# Schiffbaukalender

def t_Schiffbaukalender(w_Schiffbaukalender):
    t_Schiffbaukalender = (2 / 3) * w_Schiffbaukalender + 0.01
    return t_Schiffbaukalender

t_Schiffbaukalender = t_Schiffbaukalender(w_Schiffbaukalender)
#print('t by Schiffbaukalender is:', t_Schiffbaukalender)


# ======================================================================================================================

# Alferijev

def t_Alferijev(w, CB):
    t_Alferijev = 0.15 + 0.85 * w - 0.38 * CB * (1 - w)
    return t_Alferijev

t_Alferijev = t_Alferijev(w, CB)
#print('t by Alferijev is:', t_Alferijev)


# ======================================================================================================================
# AVERAGE VALUE OF THE THRUST DEDUCTION CALCULATED BY APROXIMATE METHODS
# ======================================================================================================================

# Average of the THRUST DEDUCTION calculated in the section above
# In future versions the user should be able to override this value
# In the future, there should be an option to exclude (manualy and automaticly) values that dont fit

def ThrustDeduction (t_HM, t_HMR, t_Taylor1923, t_Schiffbaukalender, t_Alferijev):

    t_check = (t_HM + t_HMR + t_Taylor1923 + t_Schiffbaukalender + t_Alferijev) / 5

    Numerator_t = 0

    Denominator_t = 0

    DeviationComparator_t = MaxDeviation_t * t_check

    if abs(t_HM - t_check) <= DeviationComparator_t:
        Numerator_t += t_HM
        Denominator_t += 1

    if abs(t_HMR - t_check) <= DeviationComparator_t:
        Numerator_t += t_HMR
        Denominator_t += 1

    if abs(t_Taylor1923 - t_check) <= DeviationComparator_t:
        Numerator_t += t_Taylor1923
        Denominator_t += 1

    if abs(t_Schiffbaukalender - t_check) <= DeviationComparator_t:
        Numerator_t += t_Schiffbaukalender
        Denominator_t += 1

    if abs(t_Alferijev - t_check) <= DeviationComparator_t:
        Numerator_t += t_Alferijev
        Denominator_t += 1

    t = Numerator_t / Denominator_t
    return t

t = ThrustDeduction (t_HM, t_HMR, t_Taylor1923, t_Schiffbaukalender, t_Alferijev)
#print('The average value of thrust deduction is t =', t)
#print('')


# ======================================================================================================================
# OTHER HYDRODINAMIC COEFFICIENTS
# ======================================================================================================================

# Relative rotative efficiency
# Simplest reccomendation states that this coefficient can be taken between 0.95 and 1.0 for twin screw ships,
# and between 1.0 and 1.1 for single screw ships.

if NoPropellers == 1:
    EtaR = (1.0 + 1.1) / 2
else:
    EtaR = (0.95 + 1.0) / 2

#print('Relative rotative efficiency EtaR =', EtaR)

# Holtrop and Mennen give two reccomendations in their paper, but i need Ae/A0 for one and P/D for another

# EtaR_HM = 0.9737 + 0.111 * (CP - 0.0225 * LCB) - 0.06325 * ......


# ======================================================================================================================

# Shaft efficiency
# Reccomendation for this value is between 0.96 and 0.99

EtaS = (0.96 + 0.99) / 2
#print('Shaft efficiency coeffiscient EtaS =', EtaS)


# ======================================================================================================================

# Hull efficiency

EtaH = (1 - t) / (1 - w)
#print('Hull efficiency coeffiscient EtaH =', EtaH)


# ======================================================================================================================
# CALCULATING THE NECESSARY PROPELLER THRUST
# ======================================================================================================================

# I start this calculation with effective power. In case a method doesnt include appandage resistance,
# effective power should be increased by 2 to 3 %. For the Holtrop Mennen method, I have included calculations  for
# the appendages, but for Guldhammer and Harvald, I have left them out (I will do them in the future)
# In the future, the percentage of increase of appandage resistance should be a variable to be inputted by the user

# In the future, when more methods are available, this should be more sophisticated

EffectivePowerCruisingApp = ((EffectivePowerGHCruising * ((1.02 + 1.03) / 2)) + EffectivePowerHMCruising) / 2
#print('Effective power with appandages PE_App =', EffectivePowerCruisingApp, '[kW]')


# Once we have included the appandage resistance, we can add the additional service margine. Both of these are added
# because reccomendations usualy come from model tanks where ships are perfectly smooth and water is perfectly calm.
# The reccomendation for service margin is to add between 15 and 25 %
# In the future, the service margin should be a variable to be inputted

EffectivePowerCruisingService = EffectivePowerCruisingApp * ((1.15 + 1.25) / 2)
#print('Effective power with appandages and service margin PE_Service =', EffectivePowerCruisingService, '[kW]')


# Now that we have the power or resistance that the propeller has to overcome, we can find the necessary thrust.

T = EffectivePowerCruisingService / (SpeedCruisingMS * (1 - t))     # I am not sure if i should use V or VA here
#print('Thrust that the propeller needs to develop is T =', T, '[kN]')


