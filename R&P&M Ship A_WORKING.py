
import matplotlib.pyplot as plt
import numpy as np


# ======================================================================================================================
# SHIP PARAMETERS
# ======================================================================================================================

# In the future, the user should have an option to input these once the program initiates

LengthWL = 202.0         # [m] Length at waterline
LengthPP = 202.0         # [m] Length between perpendiculars
LengthDEP = 202.0        # [m] Submerged length of the ship (Consider the bulbus bow)
Beam = 31.2              # [m] Breadth of the ship
Draught = 6.93            # [m] Depth of the ship
DraughtFore = Draught           # [m] Depth of the ship at fore end
# In the future, this should be an independent value
DraughtStern = Draught + 1.95         # [m] Depth of the ship at the stern
# In the future, this should be an independent value
Volume = LengthWL * Beam * Draught * 0.518        # [m^3] Submerged volume of the ship
# In the future version either this or the displacement should be calculated based on water density
Displacement = 23200   # [t] Displacement of the ship
# In the future version either this or the submerged volume should be calculated based on water density

CB = 0.518               # [-] Block coefficient
CP = 0.6               # [-] Prismatic coefficient
CM = 0.9               # [-] Midship section coefficient
CWP = 0.8               # [-] Waterplane area coefficient
LCB = 0.0             # [% of LengthWL] Longitudinal center of buyancy compered to main rib

ABT = 0.0                # [m^2] Cross section area of the bulb measured on the aft perpendicular
hB = Draught / 2         # [m] Position of center of ABT above the keel line

AT = Beam * 0.5          # [m^2] Immersed area of the transom

MaxDeviation_S = 0.05    # [%] Represents how much is allowed for calculated wetted surface to deviate from
                                # average of all surfaces before it is dismissed
MaxDeviation_w = 0.2     # [%] Represents how much is allowed for calculated wake fraction to deviate from
                                # average of all wake fractions before it is mismissed
MaxDeviation_t = 0.2     # [%] Represents how much is allowed for calculated thrust deduction to deviate from
                                # average of all thrust deductions before it is mismissed

# ======================================================================================================================
# APPENDAGE PARAMETERS
# ======================================================================================================================

AppendageCoef = 0.4e-3   # [-] Appendage resistance coefficient as reccomended by ITTC
SAppendage = 20          # [m^2] Wetted area of the appandeges

D = 7.1       # [m] Propeller diameter
ShaftHeight = D / 2       # [m] Vertical distance between keel and propeller shaft

z = 6                    # [-] Number of blades on the propeller

NoPropellers = 1         # [-] Number of propellers
NoRudders = 1            # [-] Number of rudders
NoBraces = 0             # [-] Number of braces
NoBossings = 0           # [-] Number of bossings

CStern = -7              # [-] Form of the afterbody (Shape of stern ribs) for Holtrop & Mennen method
                                # Choose this value by your opinion or feeling
                                # Pram with gondola                     CStern = -25
                                # V shaped section                      CStern = -10
                                # Normal section shape                  CStern = 0
                                # U shaped section with Hogner stern    CStern = 10


# ======================================================================================================================
# ENVIRONMENT PARAMETERS
# ======================================================================================================================

# User should have the ability to input some of them like temperature, salinity, etc...

pi = np.pi                      # Pi
e = np.e                        # I am not sure that this is a correct way to use e while programming
g = 9.81                        # [m/(s^2)] Earths gravity acceleration (Until we start building ships on Mars :) )
temp = 20                          # [o celsius] Temperature of the water

RoSalt = 1.025                  # [t/(m^3)] Salt water density (3.5% salt) depending on temperature
#RoSalt = (g * (104.83004 - 6.210858e-3 * temp - 5.976822e-4 * (temp**2) + 2.5797397e-6 * (temp**3))) / 1000

RoFresh = 1.0                   # [t/(m^3)] Fresh water density (0% salt) depending on temperature
#RoFresh = (g*(101.9492-5.503079e-3*temp-7.68434e-4*(temp**2)+3.611636e-6*(temp**3))) / 1000

NuSalt = 1.1907e-6              # [(m^2/s)] Kinematic viscosity of salt watter
NuFresh = 1.1410e-6             # [(m^2/s)] Kinematic viscosity of fresh watter


# ======================================================================================================================
# OBTAINED SHIP PARAMETERS
# ======================================================================================================================

# Coefficient of slenderness

def MRounded(LengthPP, Volume):
    return LengthPP / (Volume**(1 / 3))

MRounded = MRounded(LengthPP, Volume)


# ======================================================================================================================

# Constructive length (I think)

def LengthD(LengthPP):
    return 1.01 * LengthPP

LengthD = LengthD(LengthPP)


# ======================================================================================================================

# Speed in meters per second

SpeedMS = np.arange(1, 15, 1)
print('Speed V =', SpeedMS, '[m/s]')

SpeedCruisingMS = 12.35
print('Cruising speed V =', SpeedCruisingMS, '[m/s]')
print('')


# ======================================================================================================================

# Speed in knots

SpeedKts = SpeedMS / 0.5144
print('Speed =', SpeedKts, '[knots]')

SpeedCruisingKts = SpeedCruisingMS / 0.5144
print('Cruising speed =', SpeedCruisingKts, '[knots]')
print('')


# ======================================================================================================================

# Reynolds number

RaynoldsNo = (SpeedMS * LengthWL) / NuSalt
print('Raynolds number =', RaynoldsNo)

RaynoldsNoCruising = (SpeedCruisingMS * LengthWL) / NuSalt
print('Raynolds number for cruising speed =', RaynoldsNoCruising)
print('')


# ======================================================================================================================

# Froudes number based on waterline length

FroudeNo = SpeedMS / ((g * LengthWL)**(0.5))
print('Froudes number =', FroudeNo)

FroudeNoCruising = SpeedCruisingMS / ((g * LengthWL)**(0.5))
print('Froudes number for cruising speed =', FroudeNoCruising)
print('')


# ======================================================================================================================

# Froudes number based on submerged length

FroudeNoLDep = SpeedMS / ((g * LengthDEP)**0.5)
#print('Froudes number based on submerged length =', FroudeNoLDep)

FroudeNoLDepCruising = SpeedCruisingMS / ((g * LengthDEP)**0.5)
#print('Froudes number based on submerged length for cruising speed =', FroudeNoLDepCruising)


# ======================================================================================================================
# APPROXIMATE METHODS OF CALCULATION OF THE WETTED SURFACE OF THE SHIP
# ======================================================================================================================

# SSPA

def S_SSPA(LengthWL, Volume, CB, Beam, Draught):
    if 0.525 <= CB <= 0.650:
        return (3.85945 + 0.515 * (LengthWL / (Volume**(1/3)))-1.05 * CB - 0.018 * (Beam / Draught))**(Volume**(2/3))
    elif 0.650 <= CB <= 0.725:
        return (3.85945 + 0.550 * (LengthWL / (Volume**(1 / 3))) - 1.05 * CB - 0.018 * (Beam / Draught)) * (
                    Volume ** (2 / 3))
    else:
        return 0.0


S_SSPA = S_SSPA(LengthWL, Volume, CB, Beam, Draught)
#print('Wetted surface according to SSPA method =', S_SSPA, '[m^2]')

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


# ======================================================================================================================
# ASSESMENT OF USABILITY OF METHODS FOR CALCULATING THE RESISTANCE OF THE SHIP
# ======================================================================================================================

# Every method has a certain range of Froude numbers for which it applies,
# but that can be considered after the resistence has been calculated

# ======================================================================================================================

# TAYLOR METHOD

# All the ships that Admiral David Taylor had tested had exactly CM=0.925 and LCB=0.
# Even though these values are what defines this standard series, they can be ignored
# if the ship that is being tested is reasonably close to these values.

def TaylorCheck(MRounded, Beam, Draught, CP):
    if 5.2 <= MRounded <= 10.0:
        Taylor_1 = True
    else:
        Taylor_1 = False

    if 2.25 <= Beam / Draught <= 3.75:
        Taylor_2 = True
    else:
        Taylor_2 = False

    if 0.48 <= CP <= 0.86:
        Taylor_3 = True
    else:
        Taylor_3 = False

    if Taylor_1 == True and Taylor_2 == True and Taylor_3 == True:
        Taylor = True
    else:
        Taylor = False
    return Taylor


Taylor = TaylorCheck(MRounded, Beam, Draught, CP)

if Taylor == True:
    print('Using The Taylor method is acceptable')
else:
    print('Using The Taylor method is not acceptable')


# ======================================================================================================================

# LAP - KELLER METHOD

# One of the conditions is Volume/((CP*LengthD)**(1/2)) ,but that doesnt make sense, so I am ignoring it for now

def LapKellerCheck(Beam, Draught, LengthD, CP, LCB):
    if 2.0 <= Beam / Draught <= 3.3:
        LapKeller_1 = True
    else:
        LapKeller_1 = False

    if 5.0 <= LengthD / Beam <= 8.0:
        LapKeller_2 = True
    else:
        LapKeller_2 = False

    if 0.6 <= CP <= 0.85:
        LapKeller_3 = True
    else:
        LapKeller_3 = False

    if -2 <= LCB <= 3:
        LapKeller_4 = True
    else:
        LapKeller_4 = False

    if LapKeller_1 == True and LapKeller_2 == True and LapKeller_3 == True and LapKeller_4 == True:
        LapKeller = True
    else:
        LapKeller = False
    return LapKeller


LapKeller = LapKellerCheck(Beam, Draught, LengthD, CP, LCB)

if LapKeller == True:
    print('Using The Lap - Keller method is acceptable')
else:
    print('Using The Lap - Keller method is not acceptable')


# ======================================================================================================================

# SSPA METHOD

def SSPACheck(CB, MRounded, Beam, Draught, LCB):
    if 0.526 <= CB <= 0.725:
        SSPA_1 = True
    else:
        SSPA_1 = False

    if 5.06 <= MRounded <= 6.89:
        SSPA_2 = True
    else:
        SSPA_2 = False

    if 2.1 <= Beam / Draught <= 3.0:
        SSPA_3 = True
    else:
        SSPA_3 = False

    if -4 <= LCB <= 1:
        SSPA_4 = True
    else:
        SSPA_4 = False

    if SSPA_1 == True and SSPA_2 == True and SSPA_3 == True and SSPA_4 == True:
        SSPA = True
    else:
        SSPA = False
    return SSPA


SSPA = SSPACheck(CB, MRounded, Beam, Draught, LCB)

if SSPA == True:
    print('Using The SSPA method is acceptable')
else:
    print('Using The SSPA method is not acceptable')


# ======================================================================================================================

# GULDHAMMER - HARVALD METHOD

def GHCheck(CP, MRounded,):
    if 0.5 <= CP <= 0.8:
        GH_1 = True
    else:
        GH_1 = False

    if 4.0 <= MRounded <= 8.0:
        GH_2 = True
    else:
        GH_2 = False

    if GH_1 == True and GH_2 == True:
        GH = True
    else:
        GH = False
    return GH


GH = GHCheck(CP, MRounded,)

if GH == True:
    print('Using The Guldhammer - Harvald method is acceptable')
else:
    print('Using The Guldhammer - Harvald method is not acceptable')


# ======================================================================================================================

# S-60 METHOD
# It is also necessary to check in the diagrams, but ill do it in the future

def S60Check(LengthWL, Beam, CB, Draught, LengthPP, LCB):
    if 5.5 <= LengthWL / Beam <= 8.5:
        S60_1 = True
    else:
        S60_1 = False

    if 0.6 <= CB <= 0.8:
        S60_2 = True
    else:
        S60_2 = False

    if 2.5 <= Beam / Draught <= 3.5:
        S60_3 = True
    else:
        S60_3 = False

    if 45 <= LengthPP <= 300:
        S60_4 = True
    else:
        S60_4 = False

    if -2.48 <= LCB <= 3.51:
        S60_5 = True
    else:
        S60_5 = False

    if S60_1 == True and S60_2 == True and S60_3 == True and S60_4 == True and S60_5 == True:
        S60 = True
    else:
        S60 = False
    return S60


S60 = S60Check(LengthWL, Beam, CB, Draught, LengthPP, LCB)

if S60 == True:
    print('Using The S-60 method is acceptable')
else:
    print('Using The S-60 method is not acceptable')


# ======================================================================================================================

# BSRA METHOD
# It is also necessary to check in the diagrams, but ill do it in the future

def BSRACheck(CB, Beam, Draught, MRounded, LCB):
    if 0.6 <= CB <= 0.8:
        BSRA_1 = True
    else:
        BSRA_1 = False

    if 2.0 <= Beam / Draught <= 3.9:
        BSRA_2 = True
    else:
        BSRA_2 = False

    if 4 <= MRounded <= 6.5:
        BSRA_3 = True
    else:
        BSRA_3 = False

    if -2.0 <= LCB <= 3.8:
        BSRA_4 = True
    else:
        BSRA_4 = False

    if BSRA_1 == True and BSRA_2 == True and BSRA_3 == True and BSRA_4 == True:
        BSRA = True
    else:
        BSRA = False
    return BSRA


BSRA = BSRACheck(CB, Beam, Draught, MRounded, LCB)

if BSRA == True:
    print('Using The BSRA method is acceptable')
else:
    print('Using The BSRA method is not acceptable')


# ======================================================================================================================

# HOLTROP - MENNEN METHOD

def HMCheck(CP, LengthWL, Beam):
    if 0.58 <= CP <= 0.72:
        HM_1 = True
    else:
        HM_1 = False

    if 5.3 <= LengthWL / Beam <= 8.0:
        HM_2 = True
    else:
        HM_2 = False

    if HM_1 == True and HM_2 == True:
        HM = True
    else:
        HM = False
    return HM


HM = HMCheck(CP, LengthWL, Beam)

if HM == True:
    print('Using The Holtrop - Mennen method is acceptable')
else:
    print('Using The Holtrop - Mennen method is not acceptable')


# ======================================================================================================================

# HOLLENBACH METHOD

def HollenbachCheck(MRounded, CB, LengthWL, Beam, Draught, LengthDEP, LengthPP):
    if 4.49 <= MRounded <= 6.008:
        Hollenbach_1 = True
    else:
        Hollenbach_1 = False

    if 0.601 <= CB <= 0.83:
        Hollenbach_2 = True
    else:
        Hollenbach_2 = False

    if 4.71 <= LengthWL / Beam <= 7.106:
        Hollenbach_3 = True
    else:
        Hollenbach_3 = False

    if 1.989 <= Beam / Draught <= 4.002:
        Hollenbach_4 = True
    else:
        Hollenbach_4 = False

    if 1 <= LengthDEP / LengthWL <= 1.05:
        Hollenbach_5 = True
    else:
        Hollenbach_5 = False

    if 1 <= LengthWL / LengthPP <= 1.055:
        Hollenbach_6 = True
    else:
        Hollenbach_6 = False

    if Hollenbach_1 == True and Hollenbach_2 == True and Hollenbach_3 == True and Hollenbach_4 == True and Hollenbach_5 == True and Hollenbach_6 == True:
        Hollenbach = True
    else:
        Hollenbach = False
    return Hollenbach


Hollenbach = HollenbachCheck(MRounded, CB, LengthWL, Beam, Draught, LengthDEP, LengthPP)

if Hollenbach == True:
    print('Using The Hollenbach method is acceptable')
else:
    print('Using The Hollenbach method is not acceptable')

print('')

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
print('Resistance by GH =', TotalResGH, '[kN]')


def TotalResGHCruising(RoSalt, S, SpeedCruisingMS, TotalCoefGHCruising):
    TotalResGHCruising = 0.5 * RoSalt * S * SpeedCruisingMS ** 2 * TotalCoefGHCruising
    return TotalResGHCruising

TotalResGHCruising = TotalResGHCruising(RoSalt, S, SpeedCruisingMS, TotalCoefGHCruising)
print('Resistance at cruising speed by GH =', TotalResGHCruising, '[kN]')
print('')

def EffectivePowerGH(SpeedMS, TotalResGH):
    EffectivePowerGH = SpeedMS * TotalResGH
    return EffectivePowerGH

EffectivePowerGH = EffectivePowerGH(SpeedMS, TotalResGH)
print('Effective power by GH =', EffectivePowerGH, '[kW]')


def EffectivePowerGHCruising(SpeedCruisingMS, TotalResGHCruising):
    EffectivePowerGHCruising = SpeedCruisingMS * TotalResGHCruising
    return EffectivePowerGHCruising

EffectivePowerGHCruising = EffectivePowerGHCruising(SpeedCruisingMS, TotalResGHCruising)
print('Effective power at cruising speed by GH =', EffectivePowerGHCruising, '[kW]')
print('')

#plt.plot(SpeedMS, FrictionRes)
#plt.plot(SpeedMS, RemainingResGH)
#plt.plot(SpeedMS, TotalResGH)
#plt.xticks()
#plt.yticks()
#plt.ylabel("Resistance R [kN]")
#plt.xlabel("Speed V [m/s]")
#plt.grid()
#plt.show()


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
        BulbResHM = 0
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
        BulbResHM = 0
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
print('Resistance by HM =', TotalResHM, '[kN]')


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
print('Resistance at cruising speed by HM =', TotalResHMCruising, '[kN]')
print('')


def EffectivePowerHM(SpeedMS, TotalResHM):
    EffectivePowerHM = SpeedMS * TotalResHM
    return EffectivePowerHM

EffectivePowerHM = EffectivePowerHM(SpeedMS, TotalResHM)
print('Effective power by HM =', EffectivePowerHM, '[kW]')


def EffectivePowerHMCruising(SpeedCruisingMS, TotalResHMCruising):
    EffectivePowerHMCruising = SpeedCruisingMS * TotalResHMCruising
    return EffectivePowerHMCruising

EffectivePowerHMCruising = EffectivePowerHMCruising(SpeedCruisingMS, TotalResHMCruising)
print('Effective power at cruising speed by HM =', EffectivePowerHMCruising, '[kW]')
print('')

# ======================================================================================================================
# CALCULATION OF THE AVERAGE OF THE TOTAL RESISTANCE AND EFFECTIVE POWER
# ======================================================================================================================

TotalResCruising = (TotalResGHCruising+ TotalResHMCruising) / 2
print('Total resistance at cruising speed RT =', TotalResCruising, '[kN]')


EffectivePowerCruising = (EffectivePowerGHCruising + EffectivePowerHMCruising) / 2
print('Effective power at cruising speed PE =', EffectivePowerCruising, '[kW]')
print('')


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
print('The average value of wake fraction is w =', w)
print('')


# ======================================================================================================================
# CALCULATING THE SPEED OF ADVANCE
# ======================================================================================================================

AdvanceSpeedMS = SpeedCruisingMS * (1 - w)
print('Speed of advance VA =', AdvanceSpeedMS, '[m/s]')
print('')

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
print('The average value of thrust deduction is t =', t)
print('')

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
print('AE/A0 =', AEA0)
print('')



# ======================================================================================================================
# ESTIMATION OF PROPELLER EFFICIENCY FOR B SERIES PROPELLER
# ======================================================================================================================


f = open('KQ.csv', 'r')
CQ_KQ = list()
s_KQ = list()
t_KQ = list()
u_KQ = list()
v_KQ = list()

lines = f.readlines()
for line in lines:
    line = line.strip()
    line = line.replace(',', '.')
    line = line.split(";")
    CQ_KQ.append(float(line[0]))
    s_KQ.append(float(line[1]))
    t_KQ.append(float(line[2]))
    u_KQ.append(float(line[3]))
    v_KQ.append(float(line[4]))
f.close()

#print(CQ_KQ)
#print(s_KQ)
#print(t_KQ)
#print(u_KQ)
#print(v_KQ)


f = open('KT.csv', 'r')
CT_KT = list()
s_KT = list()
t_KT = list()
u_KT = list()
v_KT = list()

lines = f.readlines()
for line in lines:
    line = line.strip()
    line = line.replace(',', '.')
    line = line.split(";")
    CT_KT.append(float(line[0]))
    s_KT.append(float(line[1]))
    t_KT.append(float(line[2]))
    u_KT.append(float(line[3]))
    v_KT.append(float(line[4]))
f.close()

#print(CT_KT)
#print(s_KT)
#print(t_KT)
#print(u_KT)
#print(v_KT)




#J = np.linspace(0,1.5,200)
J = np.linspace(0.1,1.2,14) # Something very bad happens if J goes over 1.2
#print('J =', J)

imaxJ = len(J) - 1          # This represents the number of iterations for J
#print('imaxJ =', imaxJ)     # This starts at 0, so there is actually one more iteration then it sais


#PD = np.linspace(0.6, 1.4, 80)
PD = np.linspace(1.04, 1.04, 1)
print('P/D =', PD)
print('')

imaxPD = len(PD) - 1        # This represents the number of iterations for PD
#print('imaxPD =', imaxPD)   # This starts at 0, so there is actually one more iteration then it sais


iJ = 0

#KTmatrix = np.array([])
#KQmatrix = np.array([])
#Eta0matrix = np.array([])
#Jmatrix = np.array([])

#KTmatrix = list([])
#KQmatrix = list([])
#Eta0matrix = list([])
#Jmatrix = list([])

KTmatrix = []
KQmatrix = []
Eta0matrix = []
Jmatrix = []
PDmatrix = []
nmatrix = []

#print('KTmatrix empty =', KTmatrix)
#print('KQmatrix empty =', KQmatrix)
#print('Eta0matrix empty =', Eta0matrix)
#print('Jmatrix empty =', Jmatrix)
#print('PDmatrix empty =', PDmatrix)
#print('nmatrix empty =', nmatrix)



while iJ <= imaxJ:
    #print('For J =', J[iJ])

    iPD = 0

    #KTlist = np.array([])
    #KQlist = np.array([])
    #Eta0list = np.array([])
    #Jlist = np.array([])

    #KTlist = list[]
    #KQlist = list([])
    #Eta0list = list([])
    #Jlist = list([])

    KTlist = []
    KQlist = []
    Eta0list = []
    Jlist = []
    PDlist = []
    nlist = []


    #print('KTlist empty =', KTlist)
    #print('KQlist empty =', KQlist)
    #print('Eta0list empty =', Eta0list)
    #print('Jlist empty =', Jlist)


    while iPD <= imaxPD:
        #print('For PD =', PD[iPD])

        Eta0 = 0
        n = 0

        iKT = 0
        imaxKT = 38
        KT = 0

        while iKT <= imaxKT:
            KT += CT_KT[iKT] * (J[iJ] ** s_KT[iKT]) * (PD[iPD] ** t_KT[iKT]) * (AEA0 ** u_KT[iKT]) * (z ** v_KT[iKT])
            iKT += 1
        #print('KT =', KT)

        #deltaKT = deltaCD * 0.3 * () / (D**2)



        #KTlist = np.append(KTlist, [KT])

        KTlist.append(KT)

        iKQ = 0
        imaxKQ = 46
        KQ = 0

        while iKQ <= imaxKQ:
            KQ += CQ_KQ[iKQ] * (J[iJ] ** s_KQ[iKQ]) * (PD[iPD] ** t_KQ[iKQ]) * (AEA0 ** u_KQ[iKQ]) * (z ** v_KQ[iKQ])
            iKQ += 1
        #print('KQ =', KQ)

        #KQlist = np.append(KQlist, [KQ])

        KQlist.append(KQ)


        #Jlist = np.append(Jlist, [J[iJ]])

        PDlist.append(PD[iPD])

        Jlist.append(J[iJ])


        Eta0 = (J[iJ] /( 2 * pi)) * (KT / KQ)
        #print('Eta0 =', Eta0)

        Eta0list.append(Eta0)


        n = AdvanceSpeedMS / (J[iJ] * D)
        #print('n =', n)

        nlist.append(n)

        iPD += 1

    #print('KT list =', KTlist)
    #print('KQ list =', KQlist)
    #print('J list =', Jlist)
    #print('PD list =', PDlist)
    #print('Eta0 list =', Eta0list)
    #print('n list =', nlist)


    #KTmatrix = np.concatenate((KTmatrix, KTlist), axis = 0)
    #KQmatrix = np.concatenate((KQmatrix, KQlist), axis = 0)
    #Jmatrix = np.concatenate((Jmatrix, Jlist), axis = 0)
    #Eta0matrix = np.concatenate((Eta0matrix, Eta0list), axis = 0)

    KTmatrix.append(KTlist)
    KQmatrix.append(KQlist)
    Jmatrix.append(Jlist)
    PDmatrix.append(PDlist)
    Eta0matrix.append(Eta0list)
    nmatrix.append(nlist)

    iJ += 1

#KTmatrix = np.reshape(imaxPD, imaxJ)
#KQmatrix = np.reshape(imaxPD, imaxJ)

#KTmatrix = np.split(KTmatrix, 3)


KTmatrix = sum(KTmatrix, [])                # THESE ARE TEMPORARY... MAYBE
KQmatrix = sum(KQmatrix, [])
Jmatrix = sum(Jmatrix, [])
PDmatrix = sum(PDmatrix, [])
Eta0matrix = sum(Eta0matrix, [])
nmatrix = sum(nmatrix, [])



#print('KTmatrix =', KTmatrix)
#print('KQmatrix =', KQmatrix)
#print('Jmatrix =', Jmatrix)
#print('PDmatrix =', PDmatrix)
#print('Eta0matrix =', Eta0matrix)
#print('nmatrix =', nmatrix)


    #KTmatrix = np.split(KTmatrix, imaxJ + 1)
    #KQmatrix = np.split(KQmatrix, imaxJ + 1)
    #Jmatrix = np.split(Jmatrix, imaxJ + 1)
    #Eta0matrix = np.split(Eta0matrix, imaxJ + 1)

    #print('KTmatrix =', KTmatrix)
    #print('KQmatrix =', KQmatrix)
    #print('Jmatrix =', Jmatrix)
    #print('Eta0matrix =', Eta0matrix)


Eta0max = np.amax(Eta0matrix)
#print('Eta0max =', Eta0max)

    #lengthofEta0matrix = len(Eta0matrix)
    #print(lengthofEta0matrix)

Eta0maxPos = Eta0matrix.index(Eta0max)
#print('Eta0maxPos is at:', Eta0maxPos)

    #Eta0maxPos = np.where(Eta0max == np.amax(Eta0max))
    #print(Eta0maxPos)

    #ListOfCoordinates = list(zip(Eta0maxPos[0], Eta0maxPos[1]))
    #print(ListOfCoordinates)

    #print('Proba:', Eta0matrix[34])

PD_ideal = PDmatrix[Eta0maxPos]
AEA0_ideal = AEA0
J_ideal = Jmatrix[Eta0maxPos]
KT_ideal = KTmatrix[Eta0maxPos]
KQ_ideal = KQmatrix[Eta0maxPos]
Eta0_ideal = Eta0matrix[Eta0maxPos]
n_ideal = nmatrix[Eta0maxPos]

print('PD_ideal =', PD_ideal)
print('AEA0_ideal =', AEA0_ideal)
print('J_ideal =', J_ideal)
print('KT_ideal =', KT_ideal)
print('KQ_ideal =', KQ_ideal)
print('Eta0_ideal =', Eta0_ideal)
print('n_ideal =', n_ideal)
print('z =', z)
print('')



# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================

# This works for calculating KT and KQ when J and PD are single values, or at the maximum one of them is a list,
# because if more then one is a list I cant multyply each combination of values this way...

#iKT = 0
#imaxKT = 38
#KT = 0
#
#while iKT <= imaxKT:
#    KT += CT_KT[iKT] * (J ** s_KT[iKT]) * (PD ** t_KT[iKT]) * (AEA0 ** u_KT[iKT]) * (z ** v_KT[iKT])
#    iKT += 1
#print('KT =', KT)
#
#
#iKQ = 0
#imaxKQ = 46
#KQ = 0
#
#while iKQ <= imaxKQ:
#    KQ += CQ_KQ[iKQ] * (J ** s_KQ[iKQ]) * (PD ** t_KQ[iKQ]) * (AEA0 ** u_KQ[iKQ]) * (z ** v_KQ[iKQ])
#    iKQ += 1
#print('KQ =', KQ)

# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================
# ======================================================================================================================

#while iPD <= imaxPD:
#    print('For PD =', PD[iPD])
#
#    iKT = 0
#    imaxKT = 38
#    KT = 0
#
#    while iKT <= imaxKT:
#        KT += CT_KT[iKT] * (J ** s_KT[iKT]) * (PD[iPD] ** t_KT[iKT]) * (AEA0 ** u_KT[iKT]) * (z ** v_KT[iKT])
#        iKT += 1
#    print('KT =', KT)
#
#    KTlist = np.append(KTlist, [KT])
#    print('KT list =', KTlist)
#
#    iKQ = 0
#    imaxKQ = 46
#    KQ = 0
#
#    while iKQ <= imaxKQ:
#        KQ += CQ_KQ[iKQ] * (J ** s_KQ[iKQ]) * (PD[iPD] ** t_KQ[iKQ]) * (AEA0 ** u_KQ[iKQ]) * (z ** v_KQ[iKQ])
#        iKQ += 1
#    print('KQ =', KQ)
#
#    KQlist = np.append(KQlist, [KQ])
#    print('KQ list =', KQlist)
#
#    iPD += 1
#
#




# ======================================================================================================================
# ESTIMATION OF PROPELLER EFFICIENCY BY HOLTROP & MENNEN METHOD... TO BE DISCUSSED
# ======================================================================================================================

# This is something that I started

#EtaS_HM = 0.99
#
#Eta0
#
#P_Effective =
#
#P_Shaft = P_Effective / (EtaR_HM * Eta0 * EtaS_HM * ((1 - t_HM) / (1 - w_HM)))



# This is copied directly from the PDF of Jamie

#Dmax = 5.4 ## metros
#ro=1026 ##kilogramos/m3
#rpm = 145
#hz=rpm/60
#estela=0.273 wake
#Vcasco=18 hull speed
#Va = Vcasco*(1-estela) *0.5144 #m/s
#inmers = 2.3   distance between shaft and free surf probably
#K = 0.2 #constante de la formula del AEAO mínimo de Keller
#J = np.linspace(0,1.5,2000)
#PD = np.linspace(0.6, 1.4, 80)
#Treal=269292 ##N
#AEAO = np.linspace(0.3, 1.5, 120)
#Z = 4
#
#coeffsblade_Kt = np.array(([0.00880496, 0, 0, 0, 0], [-0.204554, 1, 0, 0, 0], [0.166351, 0, 1, 0, 0],
#[0.158114, 0, 2, 0, 0], [-0.147581, 2, 0, 1, 0],
#[-0.481497, 1, 1, 1, 0], [0.415437, 0, 2, 1, 0], [0.0144043, 0, 0, 0, 1],
#[-0.0530054, 2, 0, 0, 1], [0.0143481, 0, 1, 0, 1],
#[0.0606826, 1, 1, 0, 1], [-0.0125894, 0, 0, 1, 1], [0.0109689, 1, 0, 1, 1],
#[-0.133698, 0, 3, 0, 0], [0.00638407, 0, 6, 0, 0],
#[-0.00132718, 2, 6, 0, 0], [0.168496, 3, 0, 1, 0], [-0.0507214, 0, 0, 2, 0],
#[0.0854559, 2, 0, 2, 0], [-0.0504475, 3, 0, 2, 0], [0.010465, 1, 6, 2, 0],
#[-0.00648272, 2, 6, 2, 0], [-0.00841728, 0, 3, 0, 1], [0.0168424, 1, 3, 0, 1],
#[-0.00102296, 3, 3, 0, 1], [-0.0317791, 0, 3, 1, 1], [0.018604, 1, 0, 2, 1],
#[-0.00410798, 0, 2, 2, 1], [-0.000606848, 0, 0, 0, 2], [-0.0049819,1,0, 0, 2],
#[0.0025983, 2, 0, 0, 2], [-0.000560528, 3, 0, 0, 2], [-0.00163652,1, 2, 0, 2],
#[-0.000328787, 1, 6, 0, 2], [0.000116502, 2, 6, 0, 2], [0.000690, 0, 0, 1, 2],
#[0.00421749, 0, 3, 1, 2], [0.0000565229, 3, 6, 1, 2], [-0.001465,0, 3, 2, 2]))
#
#coeffsblade_Kq = np.array(([0.0037936,0,0,0,0], [0.00886523,2,0,0,0], [-0.032241,1,1,0, 0],
#[0.00344778, 0, 2, 0, 0], [-0.0408811, 0, 1, 1, 0], [-0.108009, 1, 1, 1, 0],
#[-0.0885381, 2, 1, 1, 0], [0.188561, 0, 2, 1, 0],
#[-0.00370871, 1, 0, 0, 1], [0.00513696, 0, 1, 0, 1], [0.0209449, 1, 1, 0, 1],
#[0.00474319, 2, 1, 0, 1], [-0.00723408, 2, 0, 1, 1], [0.00438388, 1, 1, 1, 1],
#[-0.0269403, 0, 2, 1, 1],
#[0.0558082, 3, 0, 1, 0], [0.0161886, 0, 3, 1, 0], [0.00318086, 1, 3, 1, 0],
#[0.015896, 0, 0, 2, 0], [0.0471729, 1, 0, 2, 0], [0.0196283, 3, 0, 2, 0],
#[-0.0502782, 0, 1, 2, 0], [-0.030055, 3, 1, 2, 0],
#[0.0417122, 2, 2, 2, 0], [-0.0397722, 0, 3, 2, 0], [-0.00350024, 0, 6, 2, 0],
#[-0.0106854, 3, 0, 0, 1], [0.00110903, 3, 3, 0, 1], [-0.000313912, 0, 6,0, 1],
#[0.0035985, 3, 0, 1, 1], [-0.00142121, 0, 6, 1, 1],
#[-0.00383637, 1, 0, 2, 1], [0.0126803, 0, 2, 2, 1], [-0.00318278, 2, 3, 2, 1],
#[0.00334268, 0, 6, 2, 1], [-0.00183491, 1, 1, 0, 2], [0.000112451, 3,2,0, 2],
#[-0.0000297228, 3, 6, 0, 2],
#[0.000269551, 1, 0, 1, 2], [0.00083265, 2, 0, 1, 2], [0.00155334, 0, 2, 1, 2],
#[0.000302683, 0, 6, 1, 2], [-0.0001843, 0, 0, 2, 2], [-0.000425399,0,3,2, 2],
#[0.0000869243, 3, 3, 2, 2], [-0.0004659, 0, 6, 2, 2], [0.0000554194, 1, 6, 2, 2]))
#
#a, b = np.shape(coeffsblade_Kt) ##dimensiones de la matriz de coeffsblade_KT (39,5)
#c, d = np.shape(coeffsblade_Kq) ##dimensiones de la matriz de coeffsblade_KQ (47,5)
#
#def obtenerKT(AEAO, PD, Z, J): ##funcion que nos calcula KT para un grado de avance
#    KT=0
#    for k in range(a):
#        Kt = 1
#        for l in range(b):
#            if l==0:
#                Kt = Kt * coeffsblade_Kt[k][l]
#            if l == 1:
#                if J == 0 and coeffsblade_Kt[k][l] == 0:
#                    Kt = Kt
#                else:
#                    Kt = Kt * (J ** coeffsblade_Kt[k][l])
#            if l == 2:
#                Kt = Kt * (PD ** coeffsblade_Kt[k][l])
#            if l == 3:
#                Kt = Kt * (AEAO ** coeffsblade_Kt[k][l])
#            if l==4:
#                Kt = Kt * (Z ** coeffsblade_Kt[k][l])
#        KT=KT+Kt
#    return KT
#
#
#def obtenerKQ (AEAO, PD, Z, J):
#    KQ=0
#    for f in range(c):
#        Kq = 1
#        for ni in range(d):
#            if ni==0:
#                Kq = Kq * coeffsblade_Kq[f][ni]
#            if ni == 1:
#                if J == 0 and coeffsblade_Kq[f][ni] == 0:
#                    Kq = Kq
#                else:
#                    Kq = Kq * (J ** coeffsblade_Kq[f][ni])
#            if ni == 2:
#                Kq = Kq * (PD ** coeffsblade_Kq[f][ni])
#            if ni == 3:
#                Kq = Kq * (AEAO ** coeffsblade_Kq[f][ni])
#            if ni == 4:
#                Kq = Kq * (Z ** coeffsblade_Kq[f][ni])
#        KQ = KQ + Kq
#    return KQ
#
#u = [0, 0, 0, 0,0,0,0] ##AEAO,PD,J,nmaximo, Diametro
#nmax = 0
#for q in AEAO:
#    for y in PD:
#        for r in J:
#            if r==0: ##para grado de avance=0 el rendimiento nunca va ser máximo
#                pass
#            else:
#                Dmtro = Va / (hz * r)
#                AEAOmin = (((1.3 + 0.3 * Z)*Treal )/ (((10**5)+(ro * inmers*9.81) -1700) * (Dmtro ** 2))) + K
#                if Dmtro < Dmax and q > AEAOmin:
#                    n = (obtenerKT(q, y, Z, r) * r )/ (2.0 * np.pi * obtenerKQ(q, y, Z, r))
#                    Emp=obtenerKT(q, y, Z, r)*ro*(hz**2)*(Dmtro**4)
#                    Q=obtenerKQ(q, y, Z, r)*ro*(hz**2)*(Dmtro**5)
#                    if Emp> (Treal-10) and Emp<(Treal+10) and (obtenerKT(q, y, Z, r))>0 and obtenerKQ(q, y, Z,
    #                    r)>0: ##un error de +-10N
#                        print(q,y,r,n,Dmtro,Emp)
#                        if n > nmax :
#                            nmax = n
#                            u[0]= q
#                            u[1] = y
#                            u[2] = r
#                            u[3] = nmax
#                            u[4] = Dmtro
#                            u[5]= Emp
#                            u[6]=Q
#                        else:
#                            pass
#                    else:
#                        pass
#                else:
#                    pass
#print('La relación AEAO de la hélice es', u[0])
#print ('La relación PD de la hélice es', u[1])
#print ('El grado de avance de la hélice es', u[2])
#print ('El rendimiento máximo de la hélice es', u[3])
#print ('El diámetro de la hélice es', u[4], 'metros')
#print ('El empuje de la hélice es', u[5], 'N')
#print ('El par de la hélice es', u[6], 'N')


# ======================================================================================================================
# OLD MANEUVERING CODE FROM JAVIER
# ======================================================================================================================

from rk import RK4

#Input parameters
#===================
rho = 1025.0            #Density
U = SpeedCruisingMS       #Design speed

T = Draught                #Draught
L = LengthWL                #Length
B = Beam                #Breadth
Cb = CB               #Block Coefficient

A = L * T / 48.1                #Area of the rudder
l = 1.63                 #Aspect ratio
#w = 0.2                 #Wake fraction
Vr = U * (1 - w)        #Effective speed on the rudder

m = Cb * L*B*T*rho      #Mass
mx = 0.05 * m  # Ranges between 0.035 - 0.05
my = 0.2 * m  # Ranges between 0.2 - 0.375

k = 0.25 * L            #Center of Rotation for the ship
Inertia = m * k**2

Fn = 0.5 * rho * (6.13*l/(l+2.25)) * A * Vr**2.
delta = 35.0 * np.pi/180

#Propeller data
Kt = KT_ideal
#D = 1.0
n = n_ideal
tpo = t

def udot(t,u,v,r):
    '''
    Computes the surge equation.
    :param t: time.
    :param u: surge velocity.
    :param v: sway velocity.
    :param r: yaw velocity.
    :return: surge acceleration
    '''
    Xu = TotalResCruising * 1e3
    Xp = (1.0 - tpo) * rho * n * n * D**4. * Kt
    cm = 0.5                               #Variable ranging 0.5 - 0.75

    udot = ( (m + cm * my) * v * r         #Added mass term
             + Xu                          #Resistance dependant on velocity. (Force units N m/s2)
             + Xp                          #Force due to propeller thrust
             - Fn * np.sin(delta) ) / (m + mx)    #Force due to rudder action
    return udot

def YHO(t,v,r):
    #Yvdot and Yrdot are taken from Clarke's expressions
    Ck = -1.0 * pi * (T / L) ** 2.0
    YvdotND = Ck * (1 + (0.16 * Cb * B/T) - 5.1 * (B/L)**2.0)
    YvND = Ck * (1 + 0.4 * Cb * B/T)
    YrdotND = Ck * (0.67*B/L - 0.0033 * (B/T)**2.)
    YrND = Ck * (-0.5 + (2.2 * B/L) - 0.08 * (B/T))
    Yvvi = 6.4241 * ((1 - Cb) * (1 / (B / T))) - 0.0743
    Yvri = -1.8561 * ((1 - Cb) * (1 / (B / T))) + 0.4503
    Yrri = -(0.4705 * ((1 - Cb) * (1 / (B / T))) + 0.0005)
    vi = v/U
    ri = r/(L*U)
    Yho = 0.5 * rho * L * T * U * U * (YvND * vi +
                                       YrND * ri +
                                       Yvvi * vi * np.abs(vi) +
                                       Yvri * vi * np.abs(ri) +
                                       Yrri * ri * np.abs(ri))
    return Yho

def vdot(t,u,v,r):
    '''
    Computes the sway equation.
    :param t: time.
    :param u: surge velocity.
    :param v: sway velocity
    :param r: yaw velocity
    :return: sway acceleration
    '''
    Yho = YHO(t,v,r)
    Ah = 0.3
    vdot = -( (m + mx) * u * r \
           + Yho - \
           (1 + Ah) * Fn * np.cos(delta) ) / (m + my)
    return vdot

def rdot(t,u,v,r):
    '''
    Computes the yaw equation.
    :param t: time.
    :param u: surge velocity.
    :param v: sway velocity
    :param r: yaw velocity
    :return: yaw acceleration
    '''
    Ck = -1.0 * pi * (T / L) ** 2.0
    NvdotND = Ck * (1.1 * (B/L) - 0.041 * B/T)
    NvND = Ck * (0.5 + 2.4 * T/L)
    NrdotND = Ck * ( (1./12.) + (0.017 * Cb * B/T) - (0.33 * B/L))
    NrND = Ck * (0.25 - 0.56 * B/L + 0.039 * B/T)
    Nvvri = -(21369.0 *(Cb * B / L)**4 - 12886.0 * (Cb * B / L)**3 + 2880.0 * (Cb * B / L)**2 - 279.9 * (Cb * B / L) +
              10.018)
    Nvrri = -0.4457 * (Cb * (1. / (B / T))) + 0.0627
    Nrri = -(5.5648 * (Cb * B / L)**2 - 1.7362 * (Cb * B / L) + 0.1487)

    vi = v/U
    ri = r/(L*U)

    xR = 0.5 * L
    Ah = 0.3

    Yho = YHO(t, v, r)

    Nho = 0.5 * rho * L * L * T * U * U * \
           (NvND * vi +
            NrND * ri +
            Nvvri * vi * vi * ri +
            Nvrri * vi * ri * ri +
            Nrri * ri * np.abs(ri))
    rdot = (Nho + \
           Yho * xR - \
           (1+Ah) * xR * Fn * np.cos(delta) ) / Inertia 
    return rdot

fo = open("Inoue.txt","w")
header = "Write outputs from the Runge-Kutta solution for each time step" + "\n" \
        "time[s]"+"\t"+"u[m/s]"+"\t"+"v[m/s]"+"\t"+"r[rad/s]" + "\n" \
        "=============================================================\n"
fo.write(header)

lv = RK4(udot,vdot,rdot)
t, [u,v,r] = lv.solve([U,0,0], 0.01,100) # lv.solve(initialConditions, timeStep, FinalTime)

print(t[-1],u[-1],v[-1],r[-1]) # Final values

fo.close()

print(t[-1],v[-1],r[-1]) # Final values

plotr = plt.plot(t, r,'g',label="r")
plotv = plt.plot(t,v,'r',label="v")
plt.xticks()
plt.yticks()
plt.ylabel("v(m/s), r(rad/s)")
plt.xlabel("time (s)")
plt.grid()
plt.legend(loc="best")
plt.show()


# ======================================================================================================================
# USEFULL CODE
# ======================================================================================================================

# Below is code to check all the variables and their values

#print(' ')
#print(' ')
#print(' ')
#print(' ')
#print(' ')
#
#
#for name in dir():
#    myvalue = eval(name)
#    print(name, "is", type(name), "and is equal to ", myvalue)


# ======================================================================================================================

# Below is code to check what kind of data is in question

#print(type(KTmatrix))



# ======================================================================================================================
# TESTING
# ======================================================================================================================



#proba1 = np.linspace(1,20,20)
#print('proba1 =', proba1)
#
#
#proba2 = np.linspace(0, 50, 8)
#print('proba2 =', proba2)
#
#bla = []
#for i in range(0, len(proba1)):
#    bla.append(proba1[i] * proba2[i])
#
#print('bla =', bla)


# ======================================================================================================================
# MANEUVERING NOMENCLATURE ACCORDING TO INOUE
# ======================================================================================================================

#Ad          # Advance
#AR          # Rudder area (immersed part bellow still water surface)
#AR0         # Rudder area
#aH          # Ratio of hydrodinamic forcce, induced on ship hull by rudder action, to rudder force
#B           # Breadth of ship
#CB          # Block coefficient
#CP          # Propeller flow rectification coefficient
#CS          # Ship hull flow rectification coefficient
#D           # Propeller diameter
#DN          # New course distance
#Dt          # Tactical diameter
#d           # Draft of ship (mean draft)
#db          # Draft at ballast condition (Mean draft)
#df          # Draft at full load condition
#FN          # Rudder normal force
#GZ_phi      # Restoring moment lever of roll
#H           # Rudder heifht
#hM          # vertical distance from still water surface to point on which lateral force a
#IXX         # moment of inertia of ship with respect to x axis
#IZZ         # moment of inertia of ship with respect to z axis
#Ipp         # moment of rotary inertia of propeller-shafting system
#JXX         # added moment of inertia of ship with respect to x axis
#JZZ         # added moment of inertia of ship with respect to z axis
#Jpp         # added moment of rotary inertia of propeher
#L           # length of ship (between perpendiculars)
#m           # mass of ship
#mx          # added mass of ship in x axis
#my          # added mass of ship in y axis
#N_phi_dot   # roll damping moment
#n           # number of propeller revolution
#P           # propeher pitch
#r           # tuming rate
#r_minut     # dimensionless turning rate (= rL/V)
#Tr          # transfer
#tPO         # thrust deduction coefficient in straight running conditiones
#u           # ship speed in x-axis direction
#V           # ship speed (= {u^+ v^)'/^)
#VR          # effective rudder inflow speed
#ni          # ship speed in y-axis direction
#ni_minut    # dimensionless ship speed in y-axis direction (= ni/V)
#W           # displacement of ship
#wP          # effective propeler wake fraction
#wPO         # effective propeller wake fraction in straight running condition
#wR          # effective rudder wake fracti
#wRO         # effective rudder wake fraction in straight running condition
#xP          # x-coordinate of propeher position
#xP_minut    # dimensionless form of Xp (= Xp/L)
#xR          # x-coordinate of point on which rudder force Y_R acts
#xR_minut    # dimensionless form of xR (= xR/L)
#x_midship   # x-coordinate of midship
#zH          # z-coordinate of point on which lateral force Y_H acts
#zR          # z-coordinate of point on which rudder force Y_R acts
#alphaR      # effective rudder inflow angle
#beta        # drift angle (= - sin^(-1) v')
#gama        # flow-rectification coefficient
#delta       # rudder angle
#lambdda     # aspect ratio of rudder
#ro          # density of water
#tau         # trim quantity
#phi         # roh angle
#psi         # headmg angle
#psi2        # new course angle


# ======================================================================================================================
# MY ATEMPT TO DO MANEUVERING
# ======================================================================================================================


#udot = ((X_H + X_P + X_R) / mass) + ni * r



#vdot = ((Y_H + Y_R) / mass) - u * r




























