import matplotlib.pyplot as plt
import numpy as np


from Input import RoSalt
from Input import SpeedMS
from Input import SpeedCruisingMS

from Input import RaynoldsNo
from Input import RaynoldsNoCruising

from Wetted_Surface import S


# ======================================================================================================================
# CALCULATING THE FRICTION RESISTENCE ITTC-1957
# ======================================================================================================================

def FrictionCoef(RaynoldsNo):
    return 0.075 / ((np.log10(RaynoldsNo) - 2) ** 2)

FrictionCoef = FrictionCoef(RaynoldsNo)
#print('Friction coefficient =', FrictionCoef)


def FrictionCoefCruising(RaynoldsNoCruising):
    return 0.075 / ((np.log10(RaynoldsNoCruising) - 2) ** 2)

FrictionCoefCruising = FrictionCoefCruising(RaynoldsNoCruising)
#print('Friction coefficient for cruising speed=', FrictionCoefCruising)


# ======================================================================================================================

def FrictionRes(RoSalt, S, SpeedMS, FrictionCoef):
    return 0.5 * RoSalt * S * (SpeedMS**2) * FrictionCoef

FrictionRes = FrictionRes(RoSalt, S, SpeedMS, FrictionCoef)
#print('Friction resistance =', FrictionRes, '[kN]')


def FrictionResCruising(RoSalt, S, SpeedCruisingMS, FrictionCoefCruising):
    return 0.5 * RoSalt * S * (SpeedCruisingMS**2) * FrictionCoefCruising

FrictionResCruising = FrictionResCruising(RoSalt, S, SpeedCruisingMS, FrictionCoefCruising)
#print('Friction resistance for cruising speed =', FrictionResCruising, '[kN]')

