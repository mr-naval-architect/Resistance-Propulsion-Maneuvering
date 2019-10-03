import matplotlib.pyplot as plt
import numpy as np


from Input import SpeedMS


# ======================================================================================================================
# AVERAGE VALUE OF THE WETTED SURFACE CALCULATED BY APROXIMATE METHODS
# ======================================================================================================================

print('')


from Wetted_Surface import S
print('The average value of submerged surfaces is', S, '[m^2]')


print('---------------------------------------------------------------------------------------------------------------')
print('')



# ======================================================================================================================
# ASSESMENT OF USABILITY OF METHODS FOR CALCULATING THE RESISTANCE OF THE SHIP
# ======================================================================================================================

# TAYLOR METHOD

from Method_Check import Taylor

if Taylor == True:
    print('Using The Taylor method is acceptable')
else:
    print('Using The Taylor method is NOT acceptable')


# ======================================================================================================================

# LAP - KELLER METHOD

from Method_Check import LapKeller

if LapKeller == True:
    print('Using The Lap - Keller method is acceptable')
else:
    print('Using The Lap - Keller method is NOT acceptable')


# ======================================================================================================================

# SSPA METHOD

from Method_Check import SSPA

if SSPA == True:
    print('Using The SSPA method is acceptable')
else:
    print('Using The SSPA method is NOT acceptable')


# ======================================================================================================================

# GULDHAMMER - HARVALD METHOD

from Method_Check import GH

if GH == True:
    print('Using The Guldhammer - Harvald method is acceptable')
else:
    print('Using The Guldhammer - Harvald method is NOT acceptable')


# ======================================================================================================================

# S-60 METHOD

from Method_Check import S60

if S60 == True:
    print('Using The S-60 method is acceptable')
else:
    print('Using The S-60 method is NOT acceptable')


# ======================================================================================================================

# BSRA METHOD

from Method_Check import BSRA

if BSRA == True:
    print('Using The BSRA method is acceptable')
else:
    print('Using The BSRA method is NOT acceptable')


# ======================================================================================================================

# HOLTROP - MENNEN METHOD

from Method_Check import HM

if HM == True:
    print('Using The Holtrop - Mennen method is acceptable')
else:
    print('Using The Holtrop - Mennen method is NOT acceptable')


# ======================================================================================================================

# HOLLENBACH METHOD

from Method_Check import Hollenbach

if Hollenbach == True:
    print('Using The Hollenbach method is acceptable')
else:
    print('Using The Hollenbach method is NOT acceptable')


print('---------------------------------------------------------------------------------------------------------------')
print('')


# ======================================================================================================================
# CALCULATING THE FRICTION RESISTENCE ITTC-1957
# ======================================================================================================================

from Friction_Res import FrictionRes
print('Friction resistance =', FrictionRes, '[kN]')

print('')

from Friction_Res import FrictionResCruising
print('Friction resistance for cruising speed =', FrictionResCruising, '[kN]')


print('---------------------------------------------------------------------------------------------------------------')
print('')


# ======================================================================================================================
# GULDHAMMER - HARVALD - APPROXIMATE RESISTANCE AND POWER PREDICTION METHOD
# ======================================================================================================================

from GH_Res import TotalResGH
print('Resistance by GH =', TotalResGH, '[kN]')

print('')

from GH_Res import TotalResGHCruising
print('Resistance at cruising speed by GH =', TotalResGHCruising, '[kN]')

print('')

from GH_Res import EffectivePowerGH
print('Effective power by GH =', EffectivePowerGH, '[kW]')

print('')

from GH_Res import EffectivePowerGHCruising
print('Effective power at cruising speed by GH =', EffectivePowerGHCruising, '[kW]')


#plt.plot(SpeedMS, FrictionRes, label = "Friction Resistance")
#plt.plot(SpeedMS, RemainingResGH, label = "Remaining Resistance")
#plt.plot(SpeedMS, TotalResGH, label = "Total Resistance")
#plt.xticks()
#plt.yticks()
#plt.ylabel("Resistance R [kN]")
#plt.xlabel("Speed V [m/s]")
#plt.grid()
#plt.legend(loc="best")
#plt.show()

print('---------------------------------------------------------------------------------------------------------------')
print('')


# ======================================================================================================================
# HOLTROP & MENNEN - APPROXIMATE RESISTANCE AND POWER PREDICTION METHOD
# ======================================================================================================================

from HM_Res import TotalResHM
print('Resistance by HM =', TotalResHM, '[kN]')

print('')

from HM_Res import TotalResHMCruising
print('Resistance at cruising speed by HM =', TotalResHMCruising, '[kN]')

print('')

from HM_Res import EffectivePowerHM
print('Effective power by HM =', EffectivePowerHM, '[kW]')

print('')

from HM_Res import EffectivePowerHMCruising
print('Effective power at cruising speed by HM =', EffectivePowerHMCruising, '[kW]')


#plt.plot(SpeedMS, AppendageResHM, label = "Appendage Resistance")
#plt.plot(SpeedMS, WaveMakingResHM, label = "Wawe Making Resistance")
#plt.plot(SpeedMS, BulbResHM, label = "Bulb Resistance")
#plt.plot(SpeedMS, TransomResHM, label = "Transom Resistance")
#plt.plot(SpeedMS, CorelationResHM, label = "Corelation Resistance")
#plt.plot(SpeedMS, TotalResHM, label = "Total Resistance")
#plt.xticks()
#plt.yticks()
#plt.ylabel("Resistance R [kN]")
#plt.xlabel("Speed V [m/s]")
#plt.grid()
#plt.legend(loc="best")
#plt.show()

print('---------------------------------------------------------------------------------------------------------------')
print('')


# ======================================================================================================================
# HOLLENBACH - APPROXIMATE RESISTANCE AND POWER PREDICTION METHOD
# ======================================================================================================================

from Hollenbach_Res import TotalResHol
print('Total resistance by Hollenbach =', TotalResHol, '[kN]')

print('')

from Hollenbach_Res import TotalResHolCruising
print('Total resistance by Hollenbach =', TotalResHolCruising, '[kN]')


#plt.plot(SpeedMS, CorelationResHol, label = "Corelation Resistance")
#plt.plot(SpeedMS, FrictionRes, label = "Friction Resistance")
#plt.plot(SpeedMS, RemainingResHol, label = "Remaining Resistance")
#plt.plot(SpeedMS, TotalResHol, label = "Total Resistance")
#plt.xticks()
#plt.yticks()
#plt.ylabel("Resistance R [kN]")
#plt.xlabel("Speed V [m/s]")
#plt.grid()
#plt.legend(loc="best")
#plt.show()

print('---------------------------------------------------------------------------------------------------------------')
print('')


# ======================================================================================================================
# CALCULATION OF THE AVERAGE OF THE TOTAL RESISTANCE AND EFFECTIVE POWER
# ======================================================================================================================

from Resistance import TotalResCruising
print('Total resistance at cruising speed RT =', TotalResCruising, '[kN]')

print('')

from Resistance import EffectivePowerCruising
print('Effective power at cruising speed PE =', EffectivePowerCruising, '[kW]')


print('---------------------------------------------------------------------------------------------------------------')
print('')


# ======================================================================================================================
# HYDRODINAMIC COEFFICIENTS
# ======================================================================================================================

# WAKE FRACTION

from Hydrodinamics import w
print('The average value of wake fraction is w =', w)
#print('')


# ======================================================================================================================

# SPEED OF ADVANCE

from Hydrodinamics import AdvanceSpeedMS
print('Speed of advance VA =', AdvanceSpeedMS, '[m/s]')
#print('')


# ======================================================================================================================

# THRUST DEDUCTION

from Hydrodinamics import t
print('The average value of thrust deduction is t =', t)
#print('')


# ======================================================================================================================

# RELATIVE ROTATIVE EFFICIENCY

from Hydrodinamics import EtaR
print('Relative rotative efficiency EtaR =', EtaR)


# ======================================================================================================================

# SHAFT EFFICIENCY

from Hydrodinamics import EtaS
print('Shaft efficiency coeffiscient EtaS =', EtaS)


# ======================================================================================================================

# HULL EFFICIENCY

from Hydrodinamics import EtaH
print('Hull efficiency coeffiscient EtaH =', EtaH)


# ======================================================================================================================
# CALCULATING THE NECESSARY PROPELLER THRUST
# ======================================================================================================================

from Hydrodinamics import EffectivePowerCruisingApp
print('Effective power with appandages PE_App =', EffectivePowerCruisingApp, '[kW]')


from Hydrodinamics import EffectivePowerCruisingService
print('Effective power with appandages and service margin PE_Service =', EffectivePowerCruisingService, '[kW]')


from Hydrodinamics import T
print('Thrust that the propeller needs to develop is T =', T, '[kN]')


print('')


# ======================================================================================================================
# CAVITATION
# ======================================================================================================================

# Kellers formula

from Cavitation import AEA0
print('Minimal ratio AE/A0 according to Kellers formula is =', AEA0)


print('')


# ======================================================================================================================
# ESTIMATION OF PROPELLER EFFICIENCY FOR B SERIES PROPELLER
# ======================================================================================================================


from Propulsion import PD_ideal
print('PD_ideal =', PD_ideal)


from Propulsion import AEA0_ideal
print('AEA0_ideal =', AEA0_ideal)


from Propulsion import J_ideal
print('J_ideal =', J_ideal)


from Propulsion import KT_ideal
print('KT_ideal =', KT_ideal)


from Propulsion import KQ_ideal
print('KQ_ideal =', KQ_ideal)


from Propulsion import Eta0_ideal
print('Eta0_ideal =', Eta0_ideal)


from Propulsion import n_ideal
print('n_ideal =', n_ideal)


from Propulsion import z
print('z =', z)


print('')


# ======================================================================================================================
# OLD MANEUVERING CODE FROM JAVIER
# ======================================================================================================================


from Maneuvering import t
from Maneuvering import u
from Maneuvering import v
from Maneuvering import r
from Maneuvering import fo
from Maneuvering import Y
from Maneuvering import X


print(t[-1],u[-1],v[-1],r[-1]) # Final values

fo.close()

plt.figure(1)
plt.subplot(121)
plotu = plt.plot(t,u,'b',label="u")
plotr = plt.plot(t, r,'g',label="r")
plotv = plt.plot(t,v,'r',label="v")
#plotpsi = plt.plot(t,P,'y',label="psi")
plt.xticks()
plt.yticks()
plt.ylabel("u(m/s),v(m/s), r(rad/s)")
plt.xlabel("time (s)")
plt.grid()
plt.legend(loc="best")
plt.subplot(122)
plotT = plt.plot(Y,X,'k--',lw=2)
plt.xticks()
plt.yticks()
plt.ylabel("x/L")
plt.xlabel("y/L")
plt.grid()
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
#    #print(name, "is", type(name), "and is equal to ", myvalue)


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



























