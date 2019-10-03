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
NoThrusters = 0          # [-] Number of thrusters

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
#print('Speed V =', SpeedMS, '[m/s]')

SpeedCruisingMS = 12.35
#print('Cruising speed V =', SpeedCruisingMS, '[m/s]')
#print('')


# ======================================================================================================================

# Speed in knots

SpeedKts = SpeedMS / 0.5144
#print('Speed =', SpeedKts, '[knots]')

SpeedCruisingKts = SpeedCruisingMS / 0.5144
#print('Cruising speed =', SpeedCruisingKts, '[knots]')
#print('')


# ======================================================================================================================

# Reynolds number

RaynoldsNo = (SpeedMS * LengthWL) / NuSalt
#print('Raynolds number =', RaynoldsNo)

RaynoldsNoCruising = (SpeedCruisingMS * LengthWL) / NuSalt
#print('Raynolds number for cruising speed =', RaynoldsNoCruising)
#print('')


# ======================================================================================================================

# Froudes number based on waterline length

FroudeNo = SpeedMS / ((g * LengthWL)**(0.5))
#print('Froudes number =', FroudeNo)

FroudeNoCruising = SpeedCruisingMS / ((g * LengthWL)**(0.5))
#print('Froudes number for cruising speed =', FroudeNoCruising)
#print('')


# ======================================================================================================================

# Froudes number based on submerged length

FroudeNoLDep = SpeedMS / ((g * LengthDEP)**0.5)
#print('Froudes number based on submerged length =', FroudeNoLDep)

FroudeNoLDepCruising = SpeedCruisingMS / ((g * LengthDEP)**0.5)
#print('Froudes number based on submerged length for cruising speed =', FroudeNoLDepCruising)

