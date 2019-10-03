import matplotlib.pyplot as plt
import numpy as np


from Input import LengthWL
from Input import Beam
from Input import Draught

from Input import CB

from Input import D

from Input import pi

from Input import SpeedCruisingMS

from Hydrodinamics import w
from Hydrodinamics import t

from Resistance import TotalResCruising

from Propulsion import KT_ideal
from Propulsion import n_ideal


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
kj = 0.2 * L
Inertia = m * k**2
J = m * kj**2

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
             - Xu                          #Resistance dependant on velocity. (Force units N m/s2)
             + Xp                          #Force due to propeller thrust
             - Fn * np.sin(delta) ) / (m + mx)    #Force due to rudder action
    return udot

def YHO(t,v,r):
    #Yvdot and Yrdot are taken from Clarke's expressions
    Ck = -1.0 * pi * (T / L) ** 2.0
    kk = 2. * T / L
    YvdotND = Ck * (1 + (0.16 * Cb * B/T) - 5.1 * (B/L)**2.0)
    YvND = 0.5 * np.pi * kk - 1.4 * CB * B / L #Ck * (1 + 0.4 * Cb * B/T)
    YrdotND = Ck * (0.67*B/L - 0.0033 * (B/T)**2.)
    YrND = 0.15 * np.pi * kk #Ck * (-0.5 + (2.2 * B/L) - 0.08 * (B/T))
    Yvvi = 6.4241 * ((1 - Cb) * (1 / (B / T))) - 0.0743
    Yvri = -1.8561 * ((1 - Cb) * (1 / (B / T))) + 0.4503
    Yrri = -(0.4705 * ((1 - Cb) * (1 / (B / T))) + 0.0005)
    vi = v/U
    ri = r*L/U
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
    vdot = ( -(m + mx) * u * r \
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
    kk = 2. * T / L
    NvdotND = Ck * (1.1 * (B/L) - 0.041 * B/T)
    NvND = 1.0 * kk #Ck * (0.5 + 2.4 * T/L)
    NrdotND = Ck * ( (1./12.) + (0.017 * Cb * B/T) - (0.33 * B/L))
    NrND = -0.74 * kk - kk**2. #Ck * (0.25 - 0.56 * B/L + 0.039 * B/T)
    Nvvri = -(21369.0 *(Cb * B / L)**4 - 12886.0 * (Cb * B / L)**3 + 2880.0 * (Cb * B / L)**2 - 279.9 * (Cb * B / L) +
              10.018)
    Nvrri = -0.4457 * (Cb * (1. / (B / T))) + 0.0627
    Nrri = -(5.5648 * (Cb * B / L)**2 - 1.7362 * (Cb * B / L) + 0.1487)

    vi = v/U
    ri = r*L/U

    xR = 0.5 * L
    Ah = 0.3

    Yho = YHO(t, v, r)

    Nho = 0.5 * rho * L * L * T * U * U * \
           (NvND * vi +
            NrND * ri +
            Nvvri * vi * vi * ri +
            Nvrri * vi * ri * ri +
            Nrri * ri * np.abs(ri) )
    rdot = (Nho + \
            Yho * xR - \
            (1+Ah) * xR * Fn * np.cos(delta) ) / (Inertia + J)
    return rdot


fo = open("Inoue.txt","w")
header = "Write outputs from the Runge-Kutta solution for each time step" + "\n" \
        "time[s]"+"\t"+"u[m/s]"+"\t"+"v[m/s]"+"\t"+"r[rad/s]" + "\n" \
        "=============================================================\n"
fo.write(header)

lv = RK4(udot,vdot,rdot)
dt = 0.1
t, [u,v,r] = lv.solve([U,0,0], dt,60*7) # lv.solve(initialConditions, timeStep, FinalTime)

x = 0.0
y = 0.0
psi = 0.0
X = list()
Y = list()
P = list()

for i in range(len(t)):
    time = t[i]
    uo = u[i]
    ro = r[i]
    vo = v[i]
    string = ('{}\t{}\t{}\t{}\n').format(time,uo,vo,ro)
    psi -= dt * ro
    x += dt * (uo * np.cos(psi) - vo * np.sin(psi) )
    y += dt * (uo * np.sin(psi) + vo * np.cos(psi) )
    X.append(x/L)
    Y.append(y/L)
    P.append(psi*180/pi)
    fo.write(string)

#print(t[-1],u[-1],v[-1],r[-1]) # Final values

fo.close()

#plt.figure(1)
#plt.subplot(121)
#plotu = plt.plot(t,u,'b',label="u")
#plotr = plt.plot(t, r,'g',label="r")
#plotv = plt.plot(t,v,'r',label="v")
#plotpsi = plt.plot(t,P,'y',label="psi")
#plt.xticks()
#plt.yticks()
#plt.ylabel("u(m/s),v(m/s), r(rad/s)")
#plt.xlabel("time (s)")
#plt.grid()
#plt.legend(loc="best")
#plt.subplot(122)
#plotT = plt.plot(Y,X,'k--',lw=2)
#plt.xticks()
#plt.yticks()
#plt.ylabel("x/L")
#plt.xlabel("y/L")
#plt.grid()
#plt.show()



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



























