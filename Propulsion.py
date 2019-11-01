import matplotlib.pyplot as plt
import numpy as np


from Input import D
from Input import z

from Input import pi

from Hydrodinamics import AdvanceSpeedMS

from Cavitation import AEA0


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
#PD = np.linspace(1.04, 1.04, 1)
PD = np.linspace(0.7, 1.04, 34)
#print('P/D =', PD)
#print('')

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

#print('PD_ideal =', PD_ideal)
#print('AEA0_ideal =', AEA0_ideal)
#print('J_ideal =', J_ideal)
#print('KT_ideal =', KT_ideal)
#print('KQ_ideal =', KQ_ideal)
#print('Eta0_ideal =', Eta0_ideal)
#print('n_ideal =', n_ideal)
#print('z =', z)
#print('')



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
#    #print('For PD =', PD[iPD])
#
#    iKT = 0
#    imaxKT = 38
#    KT = 0
#
#    while iKT <= imaxKT:
#        KT += CT_KT[iKT] * (J ** s_KT[iKT]) * (PD[iPD] ** t_KT[iKT]) * (AEA0 ** u_KT[iKT]) * (z ** v_KT[iKT])
#        iKT += 1
#    #print('KT =', KT)
#
#    KTlist = np.append(KTlist, [KT])
#    #print('KT list =', KTlist)
#
#    iKQ = 0
#    imaxKQ = 46
#    KQ = 0
#
#    while iKQ <= imaxKQ:
#        KQ += CQ_KQ[iKQ] * (J ** s_KQ[iKQ]) * (PD[iPD] ** t_KQ[iKQ]) * (AEA0 ** u_KQ[iKQ]) * (z ** v_KQ[iKQ])
#        iKQ += 1
#    #print('KQ =', KQ)
#
#    KQlist = np.append(KQlist, [KQ])
#    #print('KQ list =', KQlist)
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
#                        #print(q,y,r,n,Dmtro,Emp)
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


#