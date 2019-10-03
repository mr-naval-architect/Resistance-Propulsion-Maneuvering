import matplotlib.pyplot as plt
import numpy as np


from Input import LengthPP
from Input import LengthWL
from Input import LengthD
from Input import LengthDEP
from Input import Beam
from Input import Draught

from Input import CB
from Input import CP
from Input import LCB

from Input import MRounded

LbyB = LengthWL / Beam
BbyT = Beam / Draught


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

#if Taylor == True:
#    print('Using The Taylor method is acceptable')
#else:
#    print('Using The Taylor method is NOT acceptable')


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

#if LapKeller == True:
#    print('Using The Lap - Keller method is acceptable')
#else:
#    print('Using The Lap - Keller method is NOT acceptable')


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

#if SSPA == True:
#    print('Using The SSPA method is acceptable')
#else:
#    print('Using The SSPA method is NOT acceptable')


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

#if GH == True:
#    print('Using The Guldhammer - Harvald method is acceptable')
#else:
#    print('Using The Guldhammer - Harvald method is NOT acceptable')


# ======================================================================================================================

# S-60 METHOD

def S60CheckBasic(LengthWL, Beam, CB, Draught, LengthPP, LCB):
    if 5.5 <= (LengthWL / Beam) <= 8.5:
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
        S60Basic = True
    else:
        S60Basic = False
    return S60Basic

S60Basic = S60CheckBasic(LengthWL, Beam, CB, Draught, LengthPP, LCB)


# Checking the diagrams

LbyB = 8.0
CB = 0.65




def S60CheckDiagrams_1(LbyB, CB):
    S60_1_1 = False
    S60_1_2 = False
    S60_1_3 = False

    if 5.5 <= LbyB < 6.5:
        if ((-0.2) * LbyB + 1.9) <= CB <= 0.8:
            S60_1_1 = True
        else:
            S60_1_1 = False

    print('S60 check 1 1 =', S60_1_1)

    if 6.5 <= LbyB < 7.5:
        if 0.6 <= CB <= 0.8:
            S60_1_2 = True
        else:
            S60_1_2 = False

    print('S60 check 1 2 =', S60_1_2)

    if 7.5 <= LbyB <= 8.5:
        if 0.6 <= CB <= ((-0.2) * (LbyB) + 2.3):
            S60_1_3 = True
        else:
            S60_1_3 = False

    print('S60 check 1 3 =', S60_1_3)

    if S60_1_1 == True or S60_1_2 == True or S60_1_3 == True:
        S60Diagrams_1 = True
    else:
        S60Diagrams_1 = False

    return S60Diagrams_1

S60Diagrams_1 = S60CheckDiagrams_1(LbyB, CB)

print('S60 check 1 =', S60Diagrams_1)


def S60CheckDiagrams_2(BbyT, CB):
    for BbyT in np.arange(2.5, 3.5):
        if 0.6 <= CB <= 0.8:
            S60Diagrams_2 = True
        else:
            S60Diagrams_2 = False

    return S60Diagrams_2

S60Diagrams_2 = S60CheckDiagrams_2(BbyT, CB)

print('S60 check 2 =', S60Diagrams_2)


def S60CheckDiagrams_3(BbyT, LengthWL, Beam):
    for BbyT in np.arange(2.5, 3.5):
        if 5.5 <= LengthWL / Beam <= 8.5:
            S60Diagrams_3 = True
        else:
            S60Diagrams_3 = False

    return S60Diagrams_3

S60Diagrams_3 = S60CheckDiagrams_3(BbyT, LengthWL, Beam)

print('S60 check 3 =', S60Diagrams_3)


def S60CheckDiagrams_4(LCB, CB):
    for LCB in np.arange(-2.5, -2.0):
        if 0.6 <= CB <= 0.1 * LCB + 0.9:
            S60_4_1 = True
        else:
            S60_4_1 = False

    for LCB in np.arange(-2.0, -0.5):
        if 0.6 <= CB <= 0.7:
            S60_4_2 = True
        else:
            S60_4_2 = False

    for LCB in np.arange(-0.5, 0.5):
        if 0.6 <= CB <= 0.05 * LCB + 0.725:
            S60_4_3 = True
        else:
            S60_4_3 = False

    for LCB in np.arange(0.5, 0.55):
        if 0.6 <= CB <= 0.25 * LCB + 0.625:
            S60_4_4 = True
        else:
            S60_4_4 = False

    for LCB in np.arange(0.55, 0.7):
        if 0.0588 * LCB + 0.5676 <= CB <= 0.25 * LCB + 0.625:
            S60_4_5 = True
        else:
            S60_4_5 = False

    for LCB in np.arange(0.7, 1.4):
        if 0.0588 * LCB + 0.5676 <= CB <= 0.8:
            S60_4_6 = True
        else:
            S60_4_6 = False

    for LCB in np.arange(1.4, 3.4):
        if 0.05 * LCB + 0.58 <= CB <= 0.8:
            S60_4_7 = True
        else:
            S60_4_7 = False

    for LCB in np.arange(3.4, 3.5):
        if 0.5 * LCB - 0.95 <= CB <= 0.8:
            S60_4_8 = True
        else:
            S60_4_8 = False

    if S60_4_1 == True or S60_4_2 == True or S60_4_3 == True or S60_4_4 == True or S60_4_5 == True or S60_4_6 == True or S60_4_7 == True or S60_4_8 == True:
        S60Diagrams_4 = True
    else:
        S60Diagrams_4 = False

    return S60Diagrams_4

S60Diagrams_4 = S60CheckDiagrams_4(LCB, CB)

print('S60 check 4 =', S60Diagrams_4)


def S60CheckDiagrams_5(LCB, LbyB):
    for LCB in np.arange(-2.5, -2.4):
        if (-3) * LCB - 0.000000000003 <= LbyB <= 0.5025 * LCB + 8.7563:
            S60_5_1 = True
        else:
            S60_5_1 = False

    for LCB in np.arange(-2.4, -0.51):
        if (-0.6349) * LCB + 5.6762 <= LbyB <= 0.5025 * LCB + 8.7563:
            S60_5_2 = True
        else:
            S60_5_2 = False

    for LCB in np.arange(-0.51, 1.42):
        if (-0.1661) * LCB + 5.9153 <= LbyB <= (-0.3782) * LCB + 8.3071:
            S60_5_3 = True
        else:
            S60_5_3 = False

    for LCB in np.arange(1.42, 2.5):
        if (-0.1661) * LCB + 5.9153 <= LbyB <= (-0.25) * LCB + 8.125:
            S60_5_4 = True
        else:
            S60_5_4 = False

    for LCB in np.arange(2.5, 3.4):
        if LCB + 3 <= LbyB <= (-0.8) * LCB + 9.5:
            S60_5_5 = True
        else:
            S60_5_5 = False

    for LCB in np.arange(3.4, 3.5):
        if LCB + 3 <= LbyB <= (-2.8) * LCB + 16.3:
            S60_5_6 = True
        else:
            S60_5_6 = False

    if S60_5_1 == True or S60_5_2 == True or S60_5_3 == True or S60_5_4 == True or S60_5_5 == True or S60_5_6 == True:
        S60Diagrams_5 = True
    else:
        S60Diagrams_5 = False

    return S60Diagrams_5

S60Diagrams_5 = S60CheckDiagrams_5(LCB, LbyB)

print('S60 check 5 =', S60Diagrams_5)


def S60CheckDiagrams_6(LCB, BbyT):
    for LCB in np.arange(-2.5, -1.6):
        if 2.5 <= BbyT <= 0.5556 * LCB + 3.8889:
            S60_6_1 = True
        else:
            S60_6_1 = False

    for LCB in np.arange(-1.6, 2.5):
        if 2.5 <= BbyT <= 3.5:
            S60_6_2 = True
        else:
            S60_6_2 = False

    for LCB in np.arange(2.5, 3.5):
        if 2.5 <= BbyT <= (-0.5) * LCB + 4.25:
            S60_6_3 = True
        else:
            S60_6_3 = False

    if S60_6_1 == True or S60_6_2 == True or S60_6_3 == True:
        S60Diagrams_6 = True
    else:
        S60Diagrams_6 = False

    return S60Diagrams_6

S60Diagrams_6 = S60CheckDiagrams_6(LCB, BbyT)

print('S60 check 6 =', S60Diagrams_6)


def S60CheckDiagrams(S60Diagrams_1, S60Diagrams_2, S60Diagrams_3, S60Diagrams_4, S60Diagrams_5, S60Diagrams_6):
    if S60Diagrams_1 == True and S60Diagrams_2 == True and S60Diagrams_3 == True and S60Diagrams_4 == True and S60Diagrams_5 == True and S60Diagrams_6 == True:
        S60Diagrams = True
    else:
        S60Diagrams = False

    return S60Diagrams

S60Diagrams = S60CheckDiagrams(S60Diagrams_1, S60Diagrams_2, S60Diagrams_3, S60Diagrams_4, S60Diagrams_5, S60Diagrams_6)


def S60Check(S60Basic, S60Diagrams):
    if S60Basic == True and S60Diagrams == True:
        S60 = True
    else:
        S60 =False

    return S60

S60 = S60Check(S60Basic, S60Diagrams)


if S60 == True:
    print('Using The S-60 method is acceptable')
else:
    print('Using The S-60 method is NOT acceptable')


# ======================================================================================================================

# BSRA METHOD

def BSRACheckBasic(CB, Beam, Draught, MRounded, LCB):
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
        BSRABasic = True
    else:
        BSRABasic = False
    return BSRABasic


BSRABasic = BSRACheckBasic(CB, Beam, Draught, MRounded, LCB)


# Checking the diagrams

def BSRACheckDiagrams_1(MRounded, CB):
    for MRounded in np.arange(4.25, 4.6):
        if (-0.0833) * MRounded + 1.0542 <= CB <= 0.2857 * MRounded - 0.5143:
            BSRA_1_1 = True
        else:
            BSRA_1_1 = False

    for MRounded in np.arange(4.6, 4.85):
        if (-0.0833) * MRounded + 1.0542 <= CB <= 0.8:
            BSRA_1_2 = True
        else:
            BSRA_1_2 = False

    for MRounded in np.arange(4.85, 5.9):
        if 0.65 <= CB <= 0.8:
            BSRA_1_3 = True
        else:
            BSRA_1_3 = False

    for MRounded in np.arange(5.9, 6.0):
        if 0.65 <= CB <= (-0.1111) * MRounded + 1.3556 or 0.5 * MRounded - 2.25 <= CB <= (-0.5) * MRounded + 3.75:
            BSRA_1_4 = True
        else:
            BSRA_1_4 = False

    for MRounded in np.arange(6.0, 6.35):
        if 0.65 <= CB <= (-0.1111) * MRounded + 1.3556:
            BSRA_1_5 = True
        else:
            BSRA_1_5 = False

    if BSRA_1_1 == True or BSRA_1_2 == True or BSRA_1_3 == True or BSRA_1_4 == True or BSRA_1_5 == True:
        BSRADiagrams_1 = True
    else:
        BSRADiagrams_1 = False

    return BSRADiagrams_1

BSRADiagrams_1 = BSRACheckDiagrams_1(MRounded, CB)

print('BSRA check 1 =', BSRADiagrams_1)


def BSRACheckDiagrams_2(BbyT, CB):
    for BbyT in np.arange(2.12, 3.95):
        if 0.65 <= CB <= 0.8:
            BSRADiagrams_2 = True
        else:
            BSRADiagrams_2 = False

    return BSRADiagrams_2

BSRADiagrams_2 = BSRACheckDiagrams_2(BbyT, CB)

print('BSRA check 2 =', BSRADiagrams_2)


def BSRACheckDiagrams_3(LCB, CB):
    for LCB in np.arange(-2.0, 0.0):
        if 0.65 <= CB <= 0.05 * LCB + 0.75:
            BSRA_3_1 = True
        else:
            BSRA_3_1 = False

    for LCB in np.arange(0.0, 0.7):
        if 0.65 <= CB <= 0.0714 * LCB + 0.75:
            BSRA_3_2 = True
        else:
            BSRA_3_2 = False

    for LCB in np.arange(0.7, 1.6):
        if 0.65 <= CB <= 0.8:
            BSRA_3_3 = True
        else:
            BSRA_3_3 = False

    for LCB in np.arange(1.6, 3.0):
        if 0.0714 * LCB + 0.5357 <= CB <= 0.8:
            BSRA_3_4 = True
        else:
            BSRA_3_4 = False

    for LCB in np.arange(3.0, 3.53):
        if 0.0943 * LCB + 0.467 <= CB <= 0.8:
            BSRA_3_5 = True
        else:
            BSRA_3_5 = False

    if BSRA_3_1 == True or BSRA_3_2 == True or BSRA_3_3 == True or BSRA_3_4 == True or BSRA_3_5 == True:
        BSRADiagrams_3 = True
    else:
        BSRADiagrams_3 = False

    return BSRADiagrams_3

BSRADiagrams_3 = BSRACheckDiagrams_3(LCB, CB)

print('BSRA check 3 =', BSRADiagrams_3)


def BSRACheckDiagrams_4(MRounded, LCB):
    for LCB in np.arange(-2.0, -0.4):
        if (-0.65) * LCB + 4.3 <= MRounded <= 0.5 * LCB + 6.6:
            BSRA_4_1 = True
        else:
            BSRA_4_1 = False

    for LCB in np.arange(-0.4, 0.0):
        if (-0.65) * LCB + 4.3 <= MRounded <= (-0.7767) * LCB + 6.0893:
            BSRA_4_2 = True
        else:
            BSRA_4_2 = False

    for LCB in np.arange(0.0, 0.63):
        if 1.3043 * LCB + 4.3 <= MRounded <= (-0.7767) * LCB + 6.0893:
            BSRA_4_3 = True
        else:
            BSRA_4_3 = False

    for LCB in np.arange(0.63, 0.69):
        if 1.3043 * LCB + 4.3 <= MRounded <= 5.6:
            BSRA_4_4 = True
        else:
            BSRA_4_4 = False

    for LCB in np.arange(0.69, 1.44):
        if 5.2 <= MRounded <= 5.6:
            BSRA_4_5 = True
        else:
            BSRA_4_5 = False

    for LCB in np.arange(1.44, 1.5):
        if (-1.7857) * LCB + 7.7714 <= MRounded <= 5.6:
            BSRA_4_6 = True
        else:
            BSRA_4_6 = False

    for LCB in np.arange(1.5, 2.0):
        if (-1.7857) * LCB + 7.7714 <= MRounded <= 0.5 * LCB + 4.85:
            BSRA_4_7 = True
        else:
            BSRA_4_7 = False

    for LCB in np.arange(2.0, 2.6):
        if 0.6536 * LCB + 2.8928 <= MRounded <= (-0.1667) * LCB +6.1833:
            BSRA_4_8 = True
        else:
            BSRA_4_8 = False

    for LCB in np.arange(2.6, 3.53):
        if 0.6536 * LCB + 2.8928 <= MRounded <= (-0.5914) * LCB + 7.2876:
            BSRA_4_9 = True
        else:
            BSRA_4_9 = False

    if BSRA_4_1 == True or BSRA_4_2 == True or BSRA_4_3 == True or BSRA_4_4 == True or BSRA_4_5 == True or BSRA_4_6 == True or BSRA_4_7 == True or BSRA_4_8 == True or BSRA_4_9 == True:
        BSRADiagrams_4 = True
    else:
        BSRADiagrams_4 = False

    return BSRADiagrams_4

BSRADiagrams_4 = BSRACheckDiagrams_4(MRounded, LCB)

print('BSRA check 4 =', BSRADiagrams_4)


def BSRACheckDiagrams_5(MRounded, BbyT):
    for BbyT in np.arange(2.12, 2.54):
        if 2.381 * BbyT - 0.8476 <= MRounded <= (-2.0238) * BbyT + 10.64:
            BSRA_5_1 = True
        else:
            BSRA_5_1 = False

    for BbyT in np.arange(2.54, 2.95):
        if (-0.9756) * BbyT + 7.678 <= MRounded <= 1.2195 * BbyT + 2.4024:
            BSRA_5_2 = True
        else:
            BSRA_5_2 = False

    for BbyT in np.arange(2.95, 3.45):
        if 0.8 * BbyT + 2.44 <= MRounded <= (-1.0) * BbyT + 8.95:
            BSRA_5_3 = True
        else:
            BSRA_5_3 = False

    for BbyT in np.arange(3.45, 3.92):
        if 5.2 <= MRounded <= 5.5:
            BSRA_5_4 = True
        else:
            BSRA_5_4 = False

    if BSRA_5_1 == True or BSRA_5_2 == True or BSRA_5_3 == True or BSRA_5_4 == True:
        BSRADiagrams_5 = True
    else:
        BSRADiagrams_5 = False

    return BSRADiagrams_5

BSRADiagrams_5 = BSRACheckDiagrams_5(MRounded, BbyT)

print('BSRA check 5 =', BSRADiagrams_5)


def BSRACheckDiagrams_6(LCB, BbyT):
    for LCB in np.arange(-2.0, -0.4):
        if 2.1 <= BbyT <= 1.125 * LCB + 4.35:
            BSRA_6_1 = True
        else:
            BSRA_6_1 = False

    for LCB in np.arange(-0.4, 2.6):
        if 2.1 <= BbyT <= 3.9:
            BSRA_6_2 = True
        else:
            BSRA_6_2 = False

    for LCB in np.arange(2.6, 3.5):
        if 2.1 <= BbyT <= (-2.0) * LCB + 9.1:
            BSRA_6_3 = True
        else:
            BSRA_6_3 = False

    if BSRA_6_1 == True or BSRA_6_2 == True or BSRA_6_3 == True:
        BSRADiagrams_6 = True
    else:
        BSRADiagrams_6 = False

    return BSRADiagrams_6


BSRADiagrams_6 = BSRACheckDiagrams_6(LCB, BbyT)

print('BSRA check 6 =', BSRADiagrams_6)


def BSRACheckDiagrams(BSRADiagrams_1, BSRADiagrams_2, BSRADiagrams_3, BSRADiagrams_4, BSRADiagrams_5, BSRADiagrams_6):
    if BSRADiagrams_1 == True and BSRADiagrams_2 == True and BSRADiagrams_3 == True and BSRADiagrams_4 == True and BSRADiagrams_5 == True and BSRADiagrams_6 == True:
        BSRADiagrams = True
    else:
        BSRADiagrams = False

    return BSRADiagrams

BSRADiagrams = BSRACheckDiagrams(BSRADiagrams_1, BSRADiagrams_2, BSRADiagrams_3, BSRADiagrams_4, BSRADiagrams_5, BSRADiagrams_6)


def BSRACheck(BSRABasic, BSRADiagrams):
    if BSRABasic == True and BSRADiagrams == True:
        BSRA = True
    else:
        BSRA =False

    return BSRA


BSRA = BSRACheck(BSRABasic, BSRADiagrams)


if BSRA == True:
    print('Using The BSRA method is acceptable')
else:
    print('Using The BSRA method is NOT acceptable')


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
    print('Using The Holtrop - Mennen method is NOT acceptable')


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
    print('Using The Hollenbach method is NOT acceptable')

#print('')