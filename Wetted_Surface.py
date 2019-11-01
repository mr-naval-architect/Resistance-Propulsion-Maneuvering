import matplotlib.pyplot as plt
import numpy as np


from Input import LengthWL
from Input import LengthPP
from Input import LengthDEP

from Input import Beam
from Input import Draught
from Input import DraughtFore
from Input import DraughtStern

from Input import D
from Input import ABT
from Input import NoRudders
from Input import NoBraces
from Input import NoBossings

from Input import CB
from Input import CM
from Input import CWP

from Input import Volume
from Input import Displacement

from Input import MaxDeviation_S


# ======================================================================================================================
# APPROXIMATE METHODS OF CALCULATION OF THE WETTED SURFACE OF THE SHIP
# ======================================================================================================================

# I had to hash SSPA out because it was causing an error. I will fix it in the future

## SSPA
#
#def S_SSPA(LengthWL, Volume, CB, Beam, Draught):
#    if 0.525 <= CB <= 0.650:
#        return (3.85945 + 0.515 * (LengthWL / (Volume**(1/3)))-1.05 * CB - 0.018 * (Beam / Draught))**(Volume**(2/3))
#    elif 0.650 <= CB <= 0.725:
#        return (3.85945 + 0.550 * (LengthWL / (Volume**(1 / 3))) - 1.05 * CB - 0.018 * (Beam / Draught)) * (
#                    Volume ** (2 / 3))
#    else:
#        return 0.0
#
#
#S_SSPA = S_SSPA(LengthWL, Volume, CB, Beam, Draught)
##print('Wetted surface according to SSPA method =', S_SSPA, '[m^2]')

S_SSPA = 0.0

# ======================================================================================================================

# BSRA

def S_BSRA(LengthPP, Beam, Draught, CB, Volume):
    return (3.371+0.296*(LengthPP/Beam)+0.437*(Beam/Draught)-0.595*CB)*(Volume**(2/3))


S_BSRA = S_BSRA(LengthPP, Beam, Draught, CB, Volume)
#print('Wetted surface according to BSRA method =', S_BSRA, '[m^2]')

# ======================================================================================================================

# S-60

def S_S60(LengthPP, Beam, Draught, CB, Volume):
    return (3.432+0.305*(LengthPP/Beam)+0.443*(Beam/Draught)-0.643*CB)*(Volume**(2/3))


S_S60 = S_S60(LengthPP, Beam, Draught, CB, Volume)
#print('Wetted surface according to S-60 method =', S_S60, '[m^2]')

# ======================================================================================================================

# Mumford_1

def S_Mumford_1(LengthPP, CB, Beam, Draught):
    return 1.025*LengthPP*(CB*Beam+1.7*Draught)


S_Mumford_1 = S_Mumford_1(LengthPP, CB, Beam, Draught)
#print('Wetted surface according to Mumford 1 method =', S_Mumford_1, '[m^2]')

# ======================================================================================================================

# Mumford_2

def S_Mumford_2(LengthWL, Draught, CB, Beam):
    return 1.7*LengthWL*Draught+CB*Beam*LengthWL


S_Mumford_2 = S_Mumford_2(LengthWL, Draught, CB, Beam)
#print('Wetted surface according to Mumford 2 method =', S_Mumford_2, '[m^2]')

# ======================================================================================================================

# Fancev

def S_Fancev(LengthWL, Draught, Beam, CB):
    return LengthWL*Draught*(0.0271*(Beam/Draught)+0.492*CB+0.958*CB*(Beam/Draught)+1.390)


S_Fancev = S_Fancev(LengthWL, Draught, Beam, CB)
#print('Wetted surface according to Fancev method =', S_Fancev, '[m^2]')

# ======================================================================================================================

# Normand_1

def S_Normand_1(LengthWL, Draught, CB, Beam):
    return LengthWL*(1.52*Draught+(0.374+0.85*(CB**2))*Beam)


S_Normand_1 = S_Normand_1(LengthWL, Draught, CB, Beam)
#print('Wetted surface according to Normand 1 method =', S_Normand_1, '[m^2]')

# ======================================================================================================================

# Normand_2

def S_Normand_2(LengthWL, Draught, CB, Beam):
    return LengthWL*(1.5*Draught+(0.09+CB)*Beam)


S_Normand_2 = S_Normand_2(LengthWL, Draught, CB, Beam)
#print('Wetted surface according to Normand 2 method =', S_Normand_2, '[m^2]')

# ======================================================================================================================

# Olsen

def S_Olsen(LengthWL, Beam, Draught, CB):
    return LengthWL*Beam*(1.22*(Draught/Beam)+0.46)*(CB+0.756)


S_Olsen = S_Olsen(LengthWL, Beam, Draught, CB)
#print('Wetted surface according to Olsen method =', S_Olsen, '[m^2]')

# ======================================================================================================================

# Froude

def S_Froude(Displacement, LengthWL):
    return ((Displacement*1.016)**(2/3))*(36.38+((1.636*(LengthWL*3.28084))/((Displacement*1.016)**(1/3))))/(3.28084**2)


S_Froude = S_Froude(Displacement, LengthWL)
#print('Wetted surface according to Froude method =', S_Froude, '[m^2]')

# ======================================================================================================================

# HSVA

def S_HSVA(LengthWL, Draught, Beam, CB):
    return (LengthWL/2)*((4*Draught+Beam)/(1.625-CB))


S_HSVA = S_HSVA(LengthWL, Draught, Beam, CB)
#print('Wetted surface according to HSVA method =', S_HSVA, '[m^2]')

# ======================================================================================================================

# Leningrad

def S_Leningrad(LengthWL, Draught, CB, Beam):
    return LengthWL*(1.36*Draught+1.13*CB*Beam)


S_Leningrad = S_Leningrad(LengthWL, Draught, CB, Beam)
#print('Wetted surface according to Leningrad method =', S_Leningrad, '[m^2]')

# ======================================================================================================================

# Taylor

def S_Taylor(CM, Draught, Beam, LengthWL, Volume):
    return 3.44*(((CM**2)*(Draught/Beam))**(1/4))*((LengthWL*Volume)**(0.5))


S_Taylor = S_Taylor(CM, Draught, Beam, LengthWL, Volume)
#print('Wetted surface according to Taylor method =', S_Taylor, '[m^2]')

# ======================================================================================================================

# Holtrop_&_Mennen

def S_Holtrop_Mennen(CB, CM, Beam, Draught, CWP, LengthWL, ABT):
    k = 0.435 + 0.4425 * CB - 0.2862 * CM - 0.003467 * (Beam / Draught) + 0.3696 * CWP
    return LengthWL*(2*Draught+Beam)*(CM**(0.5))*k+2.38*(ABT/CB)


S_Holtrop_Mennen = S_Holtrop_Mennen(CB, CM, Beam, Draught, CWP, LengthWL, ABT)
#print('Wetted surface according to Holtrop & Mennen method =', S_Holtrop_Mennen, '[m^2]')

# ======================================================================================================================

# Lap

def S_Lap(Volume, LengthWL):
    return (Volume**(1/3))*(3.4*(Volume**(1/3))+0.5*LengthWL)


S_Lap = S_Lap(Volume, LengthWL)
#print('Wetted surface according to Lap method =', S_Lap, '[m^2]')

# ======================================================================================================================

# Denny

def S_Denny(LengthWL, CB, Beam, Draught):
    return LengthWL*(CB*Beam+1.7*Draught)


S_Denny = S_Denny(LengthWL, CB, Beam, Draught)
#print('Wetted surface according to Denny method =', S_Denny, '[m^2]')

# ======================================================================================================================

# Danckwardt

def S_Danckwardt(Volume, Beam, CB, Draught):
    return (Volume/Beam)*((1.7/(CB-0.2*(CB-0.65)))+(Beam/Draught))


S_Danckwardt = S_Danckwardt(Volume, Beam, CB, Draught)
#print('Wetted surface according to Danckwardt method =', S_Danckwardt, '[m^2]')

# ======================================================================================================================

# Hollenbach - This can be further expended for ships in ballast condition and two propeller ships with and without bulb

def S_Hollenbach(LengthDEP, LengthWL, LengthPP, CB, Beam, Draught, DraughtStern, DraughtFore, D, NoRudders, NoBraces, NoBossings):
    f = open('HollenbachSurfaceRegCoef.csv', 'r')
    a0 = list()
    a1 = list()
    a2 = list()
    a3 = list()

    lines = f.readlines()
    for line in lines:
        line = line.strip()
        line = line.replace(',', '.')
        line = line.split(";")
        a0.append(float(line[0]))   # For fully loaded single propeller ships
        a1.append(float(line[1]))   # For single propeller ships sailing in ballast conditions
        a2.append(float(line[2]))   # For two propeller ships without a bulb
        a3.append(float(line[3]))   # For two propeller ships with a bulb
    f.close()

    # k is calculated only for fully loaded single propeller ship. In the future, it is desirable to expend this part

    k = a0[0] + a0[1] * (LengthDEP / LengthWL) + a0[2] * (LengthWL / LengthPP) + a0[3] * CB + a0[4] * (Beam / Draught) + \
        a0[6] * (LengthPP / Draught) + a0[7] * ((DraughtStern - DraughtFore) / LengthPP) + a0[8] * (
                    D / Draught) + a0[9] * NoRudders + a0[10] * NoBraces + a0[11] * NoBossings

    S_Hollenbach = k * LengthPP * (Beam + 2 * Draught)
    return S_Hollenbach

S_Hollenbach = S_Hollenbach(LengthDEP, LengthWL, LengthPP, CB, Beam, Draught, DraughtStern, DraughtFore, D, NoRudders, NoBraces, NoBossings)
#print('Wetted surface according to Hollenbach method =', S_Hollenbach, '[m^2]')


# ======================================================================================================================
# AVERAGE VALUE OF THE WETTED SURFACE CALCULATED BY APROXIMATE METHODS
# ======================================================================================================================

# Average of the surfaces calculated in the section above
# In future versions the user should be able to override this value
# In the future, there should be an option to exclude (manualy and automaticly) values that dont fit
# Also, all these ifs should be replaced with some while function

def WettedSurface (S_SSPA, S_BSRA, S_S60, S_Mumford_1, S_Mumford_2, S_Fancev, S_Normand_1, S_Normand_2, S_Olsen, S_Froude, S_HSVA, S_Leningrad, S_Taylor, S_Holtrop_Mennen, S_Lap, S_Denny, S_Danckwardt, S_Hollenbach):

    S_check = (S_SSPA + S_BSRA + S_S60 + S_Mumford_1 + S_Mumford_2 + S_Fancev + S_Normand_1 + S_Normand_2 + S_Olsen + S_Froude + S_HSVA + S_Leningrad + S_Taylor + S_Holtrop_Mennen + S_Lap + S_Denny + S_Danckwardt + S_Hollenbach) / 18

    Numerator_S = 0

    Denominator_S = 0

    DeviationComparator = MaxDeviation_S * S_check

    if abs(S_SSPA - S_check) <= DeviationComparator:
        Numerator_S += S_SSPA
        Denominator_S += 1

    if abs(S_BSRA - S_check) <= DeviationComparator:
        Numerator_S += S_BSRA
        Denominator_S += 1

    if abs(S_S60 - S_check) <= DeviationComparator:
        Numerator_S += S_S60
        Denominator_S += 1

    if abs(S_Mumford_1 - S_check) <= DeviationComparator:
        Numerator_S += S_Mumford_1
        Denominator_S += 1

    if abs(S_Mumford_2 - S_check) <= DeviationComparator:
        Numerator_S += S_Mumford_2
        Denominator_S += 1

    if abs(S_Fancev - S_check) <= DeviationComparator:
        Numerator_S += S_Fancev
        Denominator_S += 1

    if abs(S_Normand_1 - S_check) <= DeviationComparator:
        Numerator_S += S_Normand_1
        Denominator_S += 1

    if abs(S_Normand_2 - S_check) <= DeviationComparator:
        Numerator_S += S_Normand_2
        Denominator_S += 1

    if abs(S_Olsen - S_check) <= DeviationComparator:
        Numerator_S += S_Olsen
        Denominator_S += 1

    if abs(S_Froude - S_check) <= DeviationComparator:
        Numerator_S += S_Froude
        Denominator_S += 1

    if abs(S_HSVA - S_check) <= DeviationComparator:
        Numerator_S += S_HSVA
        Denominator_S += 1

    if abs(S_Leningrad - S_check) <= DeviationComparator:
        Numerator_S += S_Leningrad
        Denominator_S += 1

    if abs(S_Taylor - S_check) <= DeviationComparator:
        Numerator_S += S_Taylor
        Denominator_S += 1

    if abs(S_Holtrop_Mennen - S_check) <= DeviationComparator:
        Numerator_S += S_Holtrop_Mennen
        Denominator_S += 1

    if abs(S_Lap - S_check) <= DeviationComparator:
        Numerator_S += S_Lap
        Denominator_S += 1

    if abs(S_Denny - S_check) <= DeviationComparator:
        Numerator_S += S_Denny
        Denominator_S += 1

    if abs(S_Danckwardt - S_check) <= DeviationComparator:
        Numerator_S += S_Danckwardt
        Denominator_S += 1

    if abs(S_Hollenbach - S_check) <= DeviationComparator:
        Numerator_S += S_Hollenbach
        Denominator_S += 1

    S = Numerator_S / Denominator_S
    return S

S = WettedSurface (S_SSPA, S_BSRA, S_S60, S_Mumford_1, S_Mumford_2, S_Fancev, S_Normand_1, S_Normand_2, S_Olsen,
                   S_Froude, S_HSVA, S_Leningrad, S_Taylor, S_Holtrop_Mennen, S_Lap, S_Denny, S_Danckwardt, S_Hollenbach)

#print('The average value of submerged surfaces is', S, '[m^2]')

