import matplotlib.pyplot as plt
import numpy as np


from Input import LengthWL
from Input import Draught

from Input import D
from Input import ShaftHeight
from Input import z

from Input import RoSalt
from Input import g

from Hydrodinamics import T


# ======================================================================================================================
# CAVITATION
# ======================================================================================================================

# Kellers formula
# This formula gives the minimal ratio of AE and A0 so that there is no cavitation


k = 0.2 # This should be expended for two propeller ships

hV = 0.75 / 100 * LengthWL

p_atm = 101.3

p0 = p_atm + RoSalt * g * (Draught + hV - ShaftHeight)

pv = 1.75

AEA0 = ((1.3 + 0.3 * z) * T) / ((p0 - pv) * D**2) + k
#print('AE/A0 =', AEA0)
#print('')

