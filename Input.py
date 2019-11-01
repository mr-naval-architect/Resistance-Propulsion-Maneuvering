import matplotlib.pyplot as plt
import numpy as np

print('Below is a list of options on how to enter your ship parameters:')
print('(Ships A to G refer to ships used by Inoue in "A Practical Calculation Method of Ship Maneuvering Motion ")')
print('    1 - Manual paramater input')
print('    2 - Ship A (Ballast) - High-speed container carrier')
print('    3 - Ship B (Ballast) - General cargo boat (10 000 DWT)')
print('    4 - Ship C (Ballast) - ro/ro ship')
print('    5 - Ship D (Ballast) - Pure car carrier')
print('    6 - Ship E (Ballast) - Bulk carrier (70 000 DWT)')
print('    7 - Ship F (Full) - VLCC (270 000 DWT)')
print('    8 - Ship F (Ballast) - VLCC (270 000 DWT)')
print('    9 - Ship G (Full) - ULCC (370 000 DWT)')
print('    10 - My university ship')
print('Please enter the number from the list:')

ParameterInput = float(input())

if ParameterInput == 1.0:

    # ==================================================================================================================
    # SHIP PARAMETERS - MANUAL INPUT
    # ==================================================================================================================

    print('Please enter the following values:')

    print('Maximal speed for which to perform calculations (end of range of speeds) [m/s]')
    SpeedMaxMS = float(input())
    SpeedMS = np.arange(1, SpeedMaxMS, 1)
    # print('Speed V =', SpeedMS, '[m/s]')

    print('Cruising speed (specific calculations are done for this speed) [m/s]')
    SpeedCruisingMS = float(input())
    # print('Cruising speed V =', SpeedCruisingMS, '[m/s]')


    # Speed in knots

    SpeedKts = SpeedMS / 0.5144
    # print('Speed =', SpeedKts, '[knots]')

    SpeedCruisingKts = SpeedCruisingMS / 0.5144
    # print('Cruising speed =', SpeedCruisingKts, '[knots]')



    print('Length at waterline [m]:')
    LengthWL = float(input())  # [m] Length at waterline

    print('Length between perpendiculars [m]:')
    LengthPP = float(input())  # [m] Length between perpendiculars

    print('Submerged length of the ship (Consider the bulbus bow) [m]:')
    LengthDEP = float(input())  # [m] Submerged length of the ship (Consider the bulbus bow)

    print('Breadth [m]:')
    Beam = float(input())  # [m] Breadth of the ship

    print('Draught [m]:')
    Draught = float(input())  # [m] Draught of the ship
    DraughtFore = Draught  # [m] Draught of the ship at fore end
    # In the future, this should be an independent value
    DraughtStern = Draught  # [m] Draught of the ship at the stern
    # In the future, this should be an independent value

    print('Volume [m^3]:')
    Volume = float(input())  # [m^3] Submerged volume of the ship
    # In the future version either this or the displacement should be calculated based on water density

    print('Displacement [t]:')
    Displacement = float(input())  # [t] Displacement of the ship
    # In the future version either this or the submerged volume should be calculated based on water density

    print('Block coefficient [-]:')
    CB = float(input())  # [-] Block coefficient

    print('Prismatic coefficient [-]:')
    CP = float(input())  # [-] Prismatic coefficient

    print('Midship coefficient [-]:')
    CM = float(input())  # [-] Midship section coefficient

    print('Waterplane area coefficient [-]:')
    CWP = float(input())  # [-] Waterplane area coefficient

    print('Longitudinal center of buyancy in relation to the main rib [% of LengthWL]:')
    LCB = float(input())  # [% of LengthWL] Longitudinal center of buyancy in relation to the main rib

    print('Cross section area of the bulb measured on the aft perpendicular [m^2]:')
    ABT = float(input())  # [m^2] Cross section area of the bulb measured on the aft perpendicular

    hB = Draught / 2  # [m] Position of center of ABT above the keel line

    print('Immersed area of the transom [m^2]:')
    AT = float(input())  # [m^2] Immersed area of the transom

    # I will add an option for these values to be edited when I have a decent user interface. Othervise it would be too confusing

    # print('Allowance for calculated wetted surface to deviate from average of all surfaces before it is dismissed:')
    MaxDeviation_S = 0.05  # [%] Represents how much is allowed for calculated wetted surface to deviate from
    # average of all surfaces before it is dismissed
    MaxDeviation_w = 0.2  # [%] Represents how much is allowed for calculated wake fraction to deviate from
    # average of all wake fractions before it is mismissed
    MaxDeviation_t = 0.2  # [%] Represents how much is allowed for calculated thrust deduction to deviate from
    # average of all thrust deductions before it is mismissed

    # ==================================================================================================================
    # APPENDAGE PARAMETERS - MANUAL INPUT
    # ==================================================================================================================

    AppendageCoef = 0.4e-3  # [-] Appendage resistance coefficient as reccomended by ITTC

    print('Wetted area of the apandeges [m^2]:')
    SAppendage = float(input())  # [m^2] Wetted area of the appandeges

    print('Propeller diameter [m]:')
    D = float(input())  # [m] Propeller diameter
    ShaftHeight = D / 2  # [m] Vertical distance between keel and propeller shaft

    print('Number of blades on the propeller [-]:')
    z = float(input())  # [-] Number of blades on the propeller

    print('Number of propellers [-]:')
    NoPropellers = float(input())  # [-] Number of propellers

    print('Number of rudders [-]:')
    NoRudders = float(input())  # [-] Number of rudders

    print('Number of braces [-]:')
    NoBraces = float(input())  # [-] Number of braces

    print('Number of bossings [-]:')
    NoBossings = float(input())  # [-] Number of bossings

    print('Number of thrusters [-]:')
    NoThrusters = float(input())  # [-] Number of thrusters

    print('Form of the afterbody (Shape of stern ribs) for Holtrop & Mennen method [-]:')
    print('Choose this value by your opinion or feeling:')
    print('Pram with gondola                     CStern = -25')
    print('V shaped section                      CStern = -10')
    print('Normal section shape                  CStern = 0')
    print('U shaped section with Hogner stern    CStern = 10')

    CStern = float(input())  # [-] Form of the afterbody (Shape of stern ribs) for Holtrop & Mennen method
    # Choose this value by your opinion or feeling
    # Pram with gondola                     CStern = -25
    # V shaped section                      CStern = -10
    # Normal section shape                  CStern = 0
    # U shaped section with Hogner stern    CStern = 10

elif ParameterInput == 2.0:

    # ==================================================================================================================
    # SHIP PARAMETERS - SHIP A (BALLAST) - CONTAINER CARRIER
    # ==================================================================================================================



    SpeedKts = 25
    # print('Speed =', SpeedKts, '[knots]')

    SpeedCruisingMS = SpeedKts * 0.5144
    # print('Cruising speed V =', SpeedCruisingMS, '[m/s]')

    SpeedCruisingKts = SpeedCruisingMS / 0.5144
    # print('Cruising speed =', SpeedCruisingKts, '[knots]')

    SpeedMS = np.arange(1, 15, 1)
    # print('Speed V =', SpeedMS, '[m/s]')



    LengthWL = 202.0  # [m] Length at waterline
    LengthPP = 202.0  # [m] Length between perpendiculars
    LengthDEP = 202.0  # [m] Submerged length of the ship (Consider the bulbus bow)
    Beam = 31.2  # [m] Breadth of the ship
    Draught = 6.93  # [m] Depth of the ship
    DraughtFore = Draught  # [m] Depth of the ship at fore end
    DraughtStern = Draught + 1.95  # [m] Depth of the ship at the stern

    Volume = 22624.0  # [m^3] Submerged volume of the ship
    Displacement = 23200.0  # [t] Displacement of the ship

    CB = 0.518  # [-] Block coefficient
    CP = 0.6  # [-] Prismatic coefficient
    CM = 0.85  # [-] Midship section coefficient
    CWP = 0.8  # [-] Waterplane area coefficient
    LCB = 0.0  # [% of LengthWL] Longitudinal center of buyancy compered to main rib

    ABT = 0.0  # [m^2] Cross section area of the bulb measured on the aft perpendicular
    hB = Draught / 2  # [m] Position of center of ABT above the keel line

    AT = Beam * 0.5  # [m^2] Immersed area of the transom

    MaxDeviation_S = 0.05  # [%] Represents how much is allowed for calculated wetted surface to deviate from
    # average of all surfaces before it is dismissed
    MaxDeviation_w = 0.2  # [%] Represents how much is allowed for calculated wake fraction to deviate from
    # average of all wake fractions before it is mismissed
    MaxDeviation_t = 0.2  # [%] Represents how much is allowed for calculated thrust deduction to deviate from
    # average of all thrust deductions before it is mismissed

    # ==================================================================================================================
    # APPENDAGE PARAMETERS - SHIP A (BALLAST) - CONTAINER CARRIER
    # ==================================================================================================================

    AppendageCoef = 0.4e-3  # [-] Appendage resistance coefficient as reccomended by ITTC
    SAppendage = 20.0  # [m^2] Wetted area of the appandeges

    D = 7.1  # [m] Propeller diameter
    ShaftHeight = D / 2  # [m] Vertical distance between keel and propeller shaft

    z = 6  # [-] Number of blades on the propeller

    NoPropellers = 1  # [-] Number of propellers
    NoRudders = 1  # [-] Number of rudders
    NoBraces = 0  # [-] Number of braces
    NoBossings = 0  # [-] Number of bossings
    NoThrusters = 0  # [-] Number of thrusters

    CStern = -7  # [-] Form of the afterbody (Shape of stern ribs) for Holtrop & Mennen method
    # Choose this value by your opinion or feeling
    # Pram with gondola                     CStern = -25
    # V shaped section                      CStern = -10
    # Normal section shape                  CStern = 0
    # U shaped section with Hogner stern    CStern = 10

elif ParameterInput == 3.0:

    # ==================================================================================================================
    # SHIP PARAMETERS - SHIP B (BALLAST) - CARGO BOAT
    # ==================================================================================================================

    SpeedKts = 18.5
    # print('Speed =', SpeedKts, '[knots]')

    SpeedCruisingMS = SpeedKts * 0.5144
    # print('Cruising speed V =', SpeedCruisingMS, '[m/s]')

    SpeedCruisingKts = SpeedCruisingMS / 0.5144
    # print('Cruising speed =', SpeedCruisingKts, '[knots]')

    SpeedMS = np.arange(1, 15, 1)
    # print('Speed V =', SpeedMS, '[m/s]')



    LengthWL = 160.0  # [m] Length at waterline
    LengthPP = 160.0  # [m] Length between perpendiculars
    LengthDEP = 160.0  # [m] Submerged length of the ship (Consider the bulbus bow)
    Beam = 23.5  # [m] Breadth of the ship
    Draught = 5.2  # [m] Depth of the ship
    DraughtFore = Draught  # [m] Depth of the ship at fore end
    DraughtStern = Draught + 3.78  # [m] Depth of the ship at the stern

    Volume = 11731.0  # [m^3] Submerged volume of the ship
    Displacement = 12024.0  # [t] Displacement of the ship

    CB = 0.6  # [-] Block coefficient
    CP = 0.63  # [-] Prismatic coefficient
    CM = 0.97  # [-] Midship section coefficient
    CWP = 0.79  # [-] Waterplane area coefficient
    LCB = 0.0  # [% of LengthWL] Longitudinal center of buyancy compered to main rib

    ABT = 0.0  # [m^2] Cross section area of the bulb measured on the aft perpendicular
    hB = Draught / 2  # [m] Position of center of ABT above the keel line

    AT = Beam * 0.5  # [m^2] Immersed area of the transom

    MaxDeviation_S = 0.05  # [%] Represents how much is allowed for calculated wetted surface to deviate from
    # average of all surfaces before it is dismissed
    MaxDeviation_w = 1.0  # [%] Represents how much is allowed for calculated wake fraction to deviate from
    # average of all wake fractions before it is mismissed
    MaxDeviation_t = 1.0  # [%] Represents how much is allowed for calculated thrust deduction to deviate from
    # average of all thrust deductions before it is mismissed

    # ==================================================================================================================
    # APPENDAGE PARAMETERS - SHIP B (BALLAST) - CARGO BOAT
    # ==================================================================================================================

    AppendageCoef = 0.4e-3  # [-] Appendage resistance coefficient as reccomended by ITTC
    SAppendage = 10.0  # [m^2] Wetted area of the appandeges

    D = 5.7  # [m] Propeller diameter
    ShaftHeight = D / 2  # [m] Vertical distance between keel and propeller shaft

    z = 4  # [-] Number of blades on the propeller

    NoPropellers = 1  # [-] Number of propellers
    NoRudders = 1  # [-] Number of rudders
    NoBraces = 0  # [-] Number of braces
    NoBossings = 0  # [-] Number of bossings
    NoThrusters = 0  # [-] Number of thrusters

    CStern = 0.0  # [-] Form of the afterbody (Shape of stern ribs) for Holtrop & Mennen method
    # Choose this value by your opinion or feeling
    # Pram with gondola                     CStern = -25
    # V shaped section                      CStern = -10
    # Normal section shape                  CStern = 0
    # U shaped section with Hogner stern    CStern = 10

elif ParameterInput == 4.0:

    # ==================================================================================================================
    # SHIP PARAMETERS - SHIP C (BALLAST) - RO/RO
    # ==================================================================================================================

    SpeedKts = 22
    # print('Speed =', SpeedKts, '[knots]')

    SpeedCruisingMS = SpeedKts * 0.5144
    # print('Cruising speed V =', SpeedCruisingMS, '[m/s]')

    SpeedCruisingKts = SpeedCruisingMS / 0.5144
    # print('Cruising speed =', SpeedCruisingKts, '[knots]')

    SpeedMS = np.arange(1, 15, 1)
    # print('Speed V =', SpeedMS, '[m/s]')



    LengthWL = 212.0  # [m] Length at waterline
    LengthPP = 212.0  # [m] Length between perpendiculars
    LengthDEP = 212.0  # [m] Submerged length of the ship (Consider the bulbus bow)
    Beam = 32.26  # [m] Breadth of the ship
    Draught = 6.29  # [m] Depth of the ship
    DraughtFore = Draught  # [m] Depth of the ship at fore end
    DraughtStern = Draught + 1.13  # [m] Depth of the ship at the stern

    Volume = 26327.0  # [m^3] Submerged volume of the ship
    Displacement = 26985.0  # [t] Displacement of the ship

    CB = 0.612  # [-] Block coefficient
    CP = 0.64  # [-] Prismatic coefficient
    CM = 0.975  # [-] Midship section coefficient
    CWP = 0.8  # [-] Waterplane area coefficient
    LCB = 0.0  # [% of LengthWL] Longitudinal center of buyancy compered to main rib

    ABT = 0.0  # [m^2] Cross section area of the bulb measured on the aft perpendicular
    hB = Draught / 2  # [m] Position of center of ABT above the keel line

    AT = Beam * 0.5  # [m^2] Immersed area of the transom

    MaxDeviation_S = 0.05  # [%] Represents how much is allowed for calculated wetted surface to deviate from
    # average of all surfaces before it is dismissed
    MaxDeviation_w = 1.0  # [%] Represents how much is allowed for calculated wake fraction to deviate from
    # average of all wake fractions before it is mismissed
    MaxDeviation_t = 1.0  # [%] Represents how much is allowed for calculated thrust deduction to deviate from
    # average of all thrust deductions before it is mismissed

    # ==================================================================================================================
    # APPENDAGE PARAMETERS - SHIP C (BALLAST) - RO/RO
    # ==================================================================================================================

    AppendageCoef = 0.4e-3  # [-] Appendage resistance coefficient as reccomended by ITTC
    SAppendage = 20.0  # [m^2] Wetted area of the appandeges

    D = 6.6  # [m] Propeller diameter
    ShaftHeight = D / 2  # [m] Vertical distance between keel and propeller shaft

    z = 5  # [-] Number of blades on the propeller

    NoPropellers = 1  # [-] Number of propellers
    NoRudders = 1  # [-] Number of rudders
    NoBraces = 0  # [-] Number of braces
    NoBossings = 0  # [-] Number of bossings
    NoThrusters = 0  # [-] Number of thrusters

    CStern = 0.0  # [-] Form of the afterbody (Shape of stern ribs) for Holtrop & Mennen method
    # Choose this value by your opinion or feeling
    # Pram with gondola                     CStern = -25
    # V shaped section                      CStern = -10
    # Normal section shape                  CStern = 0
    # U shaped section with Hogner stern    CStern = 10


elif ParameterInput == 5.0:

    # ==================================================================================================================
    # SHIP PARAMETERS - SHIP D (BALLAST) - PURE CAR CARRIER
    # ==================================================================================================================

    SpeedKts = 20.5
    # print('Speed =', SpeedKts, '[knots]')

    SpeedCruisingMS = SpeedKts * 0.5144
    # print('Cruising speed V =', SpeedCruisingMS, '[m/s]')

    SpeedCruisingKts = SpeedCruisingMS / 0.5144
    # print('Cruising speed =', SpeedCruisingKts, '[knots]')

    SpeedMS = np.arange(1, 15, 1)
    # print('Speed V =', SpeedMS, '[m/s]')



    LengthWL = 180.0  # [m] Length at waterline
    LengthPP = 180.0  # [m] Length between perpendiculars
    LengthDEP = 180.0  # [m] Submerged length of the ship (Consider the bulbus bow)
    Beam = 32.0  # [m] Breadth of the ship
    Draught = 6.8  # [m] Depth of the ship
    DraughtFore = Draught  # [m] Depth of the ship at fore end
    DraughtStern = Draught + 1.03  # [m] Depth of the ship at the stern

    Volume = 22169.0  # [m^3] Submerged volume of the ship
    Displacement = 22723.0  # [t] Displacement of the ship

    CB = 0.566  # [-] Block coefficient
    CP = 0.61  # [-] Prismatic coefficient
    CM = 0.83  # [-] Midship section coefficient
    CWP = 0.8  # [-] Waterplane area coefficient
    LCB = 0.0  # [% of LengthWL] Longitudinal center of buyancy compered to main rib

    ABT = 0.0  # [m^2] Cross section area of the bulb measured on the aft perpendicular
    hB = Draught / 2  # [m] Position of center of ABT above the keel line

    AT = Beam * 0.5  # [m^2] Immersed area of the transom

    MaxDeviation_S = 0.05  # [%] Represents how much is allowed for calculated wetted surface to deviate from
    # average of all surfaces before it is dismissed
    MaxDeviation_w = 1.0  # [%] Represents how much is allowed for calculated wake fraction to deviate from
    # average of all wake fractions before it is mismissed
    MaxDeviation_t = 1.0  # [%] Represents how much is allowed for calculated thrust deduction to deviate from
    # average of all thrust deductions before it is mismissed

    # ==================================================================================================================
    # APPENDAGE PARAMETERS - SHIP D (BALLAST) - PURE CAR CARRIER
    # ==================================================================================================================

    AppendageCoef = 0.4e-3  # [-] Appendage resistance coefficient as reccomended by ITTC
    SAppendage = 17.0  # [m^2] Wetted area of the appandeges

    D = 6.2  # [m] Propeller diameter
    ShaftHeight = D / 2  # [m] Vertical distance between keel and propeller shaft

    z = 5  # [-] Number of blades on the propeller

    NoPropellers = 1  # [-] Number of propellers
    NoRudders = 1  # [-] Number of rudders
    NoBraces = 0  # [-] Number of braces
    NoBossings = 0  # [-] Number of bossings
    NoThrusters = 0  # [-] Number of thrusters

    CStern = 0.0  # [-] Form of the afterbody (Shape of stern ribs) for Holtrop & Mennen method
    # Choose this value by your opinion or feeling
    # Pram with gondola                     CStern = -25
    # V shaped section                      CStern = -10
    # Normal section shape                  CStern = 0
    # U shaped section with Hogner stern    CStern = 10


elif ParameterInput == 6.0:

    # ==================================================================================================================
    # SHIP PARAMETERS - SHIP E (BALLAST) - BULK CARRIER
    # ==================================================================================================================

    SpeedKts = 17.5
    # print('Speed =', SpeedKts, '[knots]')

    SpeedCruisingMS = SpeedKts * 0.5144
    # print('Cruising speed V =', SpeedCruisingMS, '[m/s]')

    SpeedCruisingKts = SpeedCruisingMS / 0.5144
    # print('Cruising speed =', SpeedCruisingKts, '[knots]')

    SpeedMS = np.arange(1, 15, 1)
    # print('Speed V =', SpeedMS, '[m/s]')



    LengthWL = 230.0  # [m] Length at waterline
    LengthPP = 230.0  # [m] Length between perpendiculars
    LengthDEP = 230.0  # [m] Submerged length of the ship (Consider the bulbus bow)
    Beam = 32.2  # [m] Breadth of the ship
    Draught = 7.24  # [m] Depth of the ship
    DraughtFore = Draught  # [m] Depth of the ship at fore end
    DraughtStern = Draught + 1.03  # [m] Depth of the ship at the stern

    Volume = 43968.0  # [m^3] Submerged volume of the ship
    Displacement = 45067.0  # [t] Displacement of the ship

    CB = 0.82  # [-] Block coefficient
    CP = 0.84  # [-] Prismatic coefficient
    CM = 0.98  # [-] Midship section coefficient
    CWP = 0.84  # [-] Waterplane area coefficient
    LCB = 0.0  # [% of LengthWL] Longitudinal center of buyancy compered to main rib

    ABT = 0.0  # [m^2] Cross section area of the bulb measured on the aft perpendicular
    hB = Draught / 2  # [m] Position of center of ABT above the keel line

    AT = Beam * 0.5  # [m^2] Immersed area of the transom

    MaxDeviation_S = 0.05  # [%] Represents how much is allowed for calculated wetted surface to deviate from
    # average of all surfaces before it is dismissed
    MaxDeviation_w = 1.0  # [%] Represents how much is allowed for calculated wake fraction to deviate from
    # average of all wake fractions before it is mismissed
    MaxDeviation_t = 1.0  # [%] Represents how much is allowed for calculated thrust deduction to deviate from
    # average of all thrust deductions before it is mismissed

    # ==================================================================================================================
    # APPENDAGE PARAMETERS - SHIP E (BALLAST) - BULK CARRIER
    # ==================================================================================================================

    AppendageCoef = 0.4e-3  # [-] Appendage resistance coefficient as reccomended by ITTC
    SAppendage = 25.0  # [m^2] Wetted area of the appandeges

    D = 6.7  # [m] Propeller diameter
    ShaftHeight = D / 2  # [m] Vertical distance between keel and propeller shaft

    z = 4  # [-] Number of blades on the propeller

    NoPropellers = 1  # [-] Number of propellers
    NoRudders = 1  # [-] Number of rudders
    NoBraces = 0  # [-] Number of braces
    NoBossings = 0  # [-] Number of bossings
    NoThrusters = 0  # [-] Number of thrusters

    CStern = 0.0  # [-] Form of the afterbody (Shape of stern ribs) for Holtrop & Mennen method
    # Choose this value by your opinion or feeling
    # Pram with gondola                     CStern = -25
    # V shaped section                      CStern = -10
    # Normal section shape                  CStern = 0
    # U shaped section with Hogner stern    CStern = 10


elif ParameterInput == 7.0:

    # ==================================================================================================================
    # SHIP PARAMETERS - SHIP F (FULL) - VLCC
    # ==================================================================================================================

    SpeedKts = 16
    # print('Speed =', SpeedKts, '[knots]')

    SpeedCruisingMS = SpeedKts * 0.5144
    # print('Cruising speed V =', SpeedCruisingMS, '[m/s]')

    SpeedCruisingKts = SpeedCruisingMS / 0.5144
    # print('Cruising speed =', SpeedCruisingKts, '[knots]')

    SpeedMS = np.arange(1, 15, 1)
    # print('Speed V =', SpeedMS, '[m/s]')



    LengthWL = 318.0  # [m] Length at waterline
    LengthPP = 318.0  # [m] Length between perpendiculars
    LengthDEP = 318.0  # [m] Submerged length of the ship (Consider the bulbus bow)
    Beam = 56.0  # [m] Breadth of the ship
    Draught = 20.58  # [m] Depth of the ship
    DraughtFore = Draught  # [m] Depth of the ship at fore end
    DraughtStern = Draught  # [m] Depth of the ship at the stern

    Volume = 303086.0  # [m^3] Submerged volume of the ship
    Displacement = 310663.0  # [t] Displacement of the ship

    CB = 0.827  # [-] Block coefficient
    CP = 0.85  # [-] Prismatic coefficient
    CM = 0.98  # [-] Midship section coefficient
    CWP = 0.84  # [-] Waterplane area coefficient
    LCB = 0.0  # [% of LengthWL] Longitudinal center of buyancy compered to main rib

    ABT = 0.0  # [m^2] Cross section area of the bulb measured on the aft perpendicular
    hB = Draught / 2  # [m] Position of center of ABT above the keel line

    AT = Beam * 0.5  # [m^2] Immersed area of the transom

    MaxDeviation_S = 0.05  # [%] Represents how much is allowed for calculated wetted surface to deviate from
    # average of all surfaces before it is dismissed
    MaxDeviation_w = 1.0  # [%] Represents how much is allowed for calculated wake fraction to deviate from
    # average of all wake fractions before it is mismissed
    MaxDeviation_t = 1.0  # [%] Represents how much is allowed for calculated thrust deduction to deviate from
    # average of all thrust deductions before it is mismissed

    # ==================================================================================================================
    # APPENDAGE PARAMETERS - SHIP F (FULL) - VLCC
    # ==================================================================================================================

    AppendageCoef = 0.4e-3  # [-] Appendage resistance coefficient as reccomended by ITTC
    SAppendage = 40.0  # [m^2] Wetted area of the appandeges

    D = 8.9  # [m] Propeller diameter
    ShaftHeight = D / 2  # [m] Vertical distance between keel and propeller shaft

    z = 5  # [-] Number of blades on the propeller

    NoPropellers = 1  # [-] Number of propellers
    NoRudders = 1  # [-] Number of rudders
    NoBraces = 0  # [-] Number of braces
    NoBossings = 0  # [-] Number of bossings
    NoThrusters = 0  # [-] Number of thrusters

    CStern = 0.0  # [-] Form of the afterbody (Shape of stern ribs) for Holtrop & Mennen method
    # Choose this value by your opinion or feeling
    # Pram with gondola                     CStern = -25
    # V shaped section                      CStern = -10
    # Normal section shape                  CStern = 0
    # U shaped section with Hogner stern    CStern = 10


elif ParameterInput == 8.0:

    # ==================================================================================================================
    # SHIP PARAMETERS - SHIP F (BALLAST) - VLCC
    # ==================================================================================================================

    SpeedKts = 18
    # print('Speed =', SpeedKts, '[knots]')

    SpeedCruisingMS = SpeedKts * 0.5144
    # print('Cruising speed V =', SpeedCruisingMS, '[m/s]')

    SpeedCruisingKts = SpeedCruisingMS / 0.5144
    # print('Cruising speed =', SpeedCruisingKts, '[knots]')

    SpeedMS = np.arange(1, 15, 1)
    # print('Speed V =', SpeedMS, '[m/s]')



    LengthWL = 318.0  # [m] Length at waterline
    LengthPP = 318.0  # [m] Length between perpendiculars
    LengthDEP = 318.0  # [m] Submerged length of the ship (Consider the bulbus bow)
    Beam = 56.0  # [m] Breadth of the ship
    Draught = 9.64  # [m] Depth of the ship
    DraughtFore = Draught  # [m] Depth of the ship at fore end
    DraughtStern = Draught + 3.95  # [m] Depth of the ship at the stern

    Volume = 135275.0  # [m^3] Submerged volume of the ship
    Displacement = 138657.0  # [t] Displacement of the ship

    CB = 0.788  # [-] Block coefficient
    CP = 0.81  # [-] Prismatic coefficient
    CM = 0.97  # [-] Midship section coefficient
    CWP = 0.81  # [-] Waterplane area coefficient
    LCB = 0.0  # [% of LengthWL] Longitudinal center of buyancy compered to main rib

    ABT = 0.0  # [m^2] Cross section area of the bulb measured on the aft perpendicular
    hB = Draught / 2  # [m] Position of center of ABT above the keel line

    AT = Beam * 0.5  # [m^2] Immersed area of the transom

    MaxDeviation_S = 0.05  # [%] Represents how much is allowed for calculated wetted surface to deviate from
    # average of all surfaces before it is dismissed
    MaxDeviation_w = 1.0  # [%] Represents how much is allowed for calculated wake fraction to deviate from
    # average of all wake fractions before it is mismissed
    MaxDeviation_t = 1.0  # [%] Represents how much is allowed for calculated thrust deduction to deviate from
    # average of all thrust deductions before it is mismissed

    # ==================================================================================================================
    # APPENDAGE PARAMETERS - SHIP F (BALLAST) - VLCC
    # ==================================================================================================================

    AppendageCoef = 0.4e-3  # [-] Appendage resistance coefficient as reccomended by ITTC
    SAppendage = 40.0  # [m^2] Wetted area of the appandeges

    D = 8.9  # [m] Propeller diameter
    ShaftHeight = D / 2  # [m] Vertical distance between keel and propeller shaft

    z = 5  # [-] Number of blades on the propeller

    NoPropellers = 1  # [-] Number of propellers
    NoRudders = 1  # [-] Number of rudders
    NoBraces = 0  # [-] Number of braces
    NoBossings = 0  # [-] Number of bossings
    NoThrusters = 0  # [-] Number of thrusters

    CStern = 0.0  # [-] Form of the afterbody (Shape of stern ribs) for Holtrop & Mennen method
    # Choose this value by your opinion or feeling
    # Pram with gondola                     CStern = -25
    # V shaped section                      CStern = -10
    # Normal section shape                  CStern = 0
    # U shaped section with Hogner stern    CStern = 10


elif ParameterInput == 9.0:

    # ==================================================================================================================
    # SHIP PARAMETERS - SHIP G (FULL) - ULCC
    # ==================================================================================================================

    SpeedKts = 14.5
    # print('Speed =', SpeedKts, '[knots]')

    SpeedCruisingMS = SpeedKts * 0.5144
    # print('Cruising speed V =', SpeedCruisingMS, '[m/s]')

    SpeedCruisingKts = SpeedCruisingMS / 0.5144
    # print('Cruising speed =', SpeedCruisingKts, '[knots]')

    SpeedMS = np.arange(1, 15, 1)
    # print('Speed V =', SpeedMS, '[m/s]')



    LengthWL = 348.0  # [m] Length at waterline
    LengthPP = 348.0  # [m] Length between perpendiculars
    LengthDEP = 348.0  # [m] Submerged length of the ship (Consider the bulbus bow)
    Beam = 63.4  # [m] Breadth of the ship
    Draught = 21.85  # [m] Depth of the ship
    DraughtFore = Draught  # [m] Depth of the ship at fore end
    DraughtStern = Draught  # [m] Depth of the ship at the stern

    Volume = 398198.0  # [m^3] Submerged volume of the ship
    Displacement = 408154.0  # [t] Displacement of the ship

    CB = 0.826  # [-] Block coefficient
    CP = 0.85  # [-] Prismatic coefficient
    CM = 0.98  # [-] Midship section coefficient
    CWP = 0.84  # [-] Waterplane area coefficient
    LCB = 0.0  # [% of LengthWL] Longitudinal center of buyancy compered to main rib

    ABT = 0.0  # [m^2] Cross section area of the bulb measured on the aft perpendicular
    hB = Draught / 2  # [m] Position of center of ABT above the keel line

    AT = Beam * 0.5  # [m^2] Immersed area of the transom

    MaxDeviation_S = 0.05  # [%] Represents how much is allowed for calculated wetted surface to deviate from
    # average of all surfaces before it is dismissed
    MaxDeviation_w = 1.0  # [%] Represents how much is allowed for calculated wake fraction to deviate from
    # average of all wake fractions before it is mismissed
    MaxDeviation_t = 1.0  # [%] Represents how much is allowed for calculated thrust deduction to deviate from
    # average of all thrust deductions before it is mismissed

    # ==================================================================================================================
    # APPENDAGE PARAMETERS - SHIP G (FULL) - ULCC
    # ==================================================================================================================

    AppendageCoef = 0.4e-3  # [-] Appendage resistance coefficient as reccomended by ITTC
    SAppendage = 45.0  # [m^2] Wetted area of the appandeges

    D = 9.6  # [m] Propeller diameter
    ShaftHeight = D / 2  # [m] Vertical distance between keel and propeller shaft

    z = 5  # [-] Number of blades on the propeller

    NoPropellers = 1  # [-] Number of propellers
    NoRudders = 1  # [-] Number of rudders
    NoBraces = 0  # [-] Number of braces
    NoBossings = 0  # [-] Number of bossings
    NoThrusters = 0  # [-] Number of thrusters

    CStern = 0.0  # [-] Form of the afterbody (Shape of stern ribs) for Holtrop & Mennen method
    # Choose this value by your opinion or feeling
    # Pram with gondola                     CStern = -25
    # V shaped section                      CStern = -10
    # Normal section shape                  CStern = 0
    # U shaped section with Hogner stern    CStern = 10


elif ParameterInput == 10.0:

    # ==================================================================================================================
    # SHIP PARAMETERS - MY UNIVERSITY SHIP
    # ==================================================================================================================

    SpeedKts = 16
    # print('Speed =', SpeedKts, '[knots]')

    SpeedCruisingMS = SpeedKts * 0.5144
    # print('Cruising speed V =', SpeedCruisingMS, '[m/s]')

    SpeedCruisingKts = SpeedCruisingMS / 0.5144
    # print('Cruising speed =', SpeedCruisingKts, '[knots]')

    SpeedMS = np.arange(1, 15, 1)
    # print('Speed V =', SpeedMS, '[m/s]')



    LengthWL = 132.7  # [m] Length at waterline
    LengthPP = 130.0  # [m] Length between perpendiculars
    LengthDEP = 132.7  # [m] Submerged length of the ship (Consider the bulbus bow)
    Beam = 20.0  # [m] Breadth of the ship
    Draught = 6.4  # [m] Depth of the ship
    DraughtFore = Draught  # [m] Depth of the ship at fore end
    DraughtStern = Draught  # [m] Depth of the ship at the stern

    Volume = 11523.8  # [m^3] Submerged volume of the ship
    Displacement = 11882.8  # [t] Displacement of the ship

    CB = 0.678  # [-] Block coefficient
    CP = 0.718  # [-] Prismatic coefficient
    CM = 0.945  # [-] Midship section coefficient
    CWP = 0.85  # [-] Waterplane area coefficient
    LCB = -1.941  # [% of LengthWL] Longitudinal center of buyancy compered to main rib

    ABT = 0.0  # [m^2] Cross section area of the bulb measured on the aft perpendicular
    hB = Draught / 2  # [m] Position of center of ABT above the keel line

    AT = Beam * 0.5  # [m^2] Immersed area of the transom

    MaxDeviation_S = 0.05  # [%] Represents how much is allowed for calculated wetted surface to deviate from
    # average of all surfaces before it is dismissed
    MaxDeviation_w = 1.0  # [%] Represents how much is allowed for calculated wake fraction to deviate from
    # average of all wake fractions before it is mismissed
    MaxDeviation_t = 1.0  # [%] Represents how much is allowed for calculated thrust deduction to deviate from
    # average of all thrust deductions before it is mismissed

    # ==================================================================================================================
    # APPENDAGE PARAMETERS - MY UNIVERSITY SHIP
    # ==================================================================================================================

    AppendageCoef = 0.4e-3  # [-] Appendage resistance coefficient as reccomended by ITTC
    SAppendage = 15.0  # [m^2] Wetted area of the appandeges

    D = 4.1  # [m] Propeller diameter
    ShaftHeight = D / 2  # [m] Vertical distance between keel and propeller shaft

    z = 4  # [-] Number of blades on the propeller

    NoPropellers = 1  # [-] Number of propellers
    NoRudders = 1  # [-] Number of rudders
    NoBraces = 0  # [-] Number of braces
    NoBossings = 0  # [-] Number of bossings
    NoThrusters = 0  # [-] Number of thrusters

    CStern = 0.0  # [-] Form of the afterbody (Shape of stern ribs) for Holtrop & Mennen method
    # Choose this value by your opinion or feeling
    # Pram with gondola                     CStern = -25
    # V shaped section                      CStern = -10
    # Normal section shape                  CStern = 0
    # U shaped section with Hogner stern    CStern = 10

else:
    print('There was an error. Please choose one of the options available')

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


## ======================================================================================================================
#
## Speed in meters per second
#
#SpeedMS = np.arange(1, 15, 1)
##print('Speed V =', SpeedMS, '[m/s]')
#
#SpeedCruisingMS = 12.35
##print('Cruising speed V =', SpeedCruisingMS, '[m/s]')
##print('')
#
#
## ======================================================================================================================
#
## Speed in knots
#
#SpeedKts = SpeedMS / 0.5144
##print('Speed =', SpeedKts, '[knots]')
#
#SpeedCruisingKts = SpeedCruisingMS / 0.5144
##print('Cruising speed =', SpeedCruisingKts, '[knots]')
##print('')
#
#
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



