import matplotlib.pyplot as plt
import numpy as np


from Input import LengthWL
from Input import Beam
from Input import Draught

from Input import D
from Input import CStern

from Input import CB
from Input import CP
from Input import LCB

from Input import MaxDeviation_t

from w import w_Schiffbaukalender
from w import w


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
