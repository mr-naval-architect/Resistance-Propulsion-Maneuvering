import matplotlib.pyplot as plt
import numpy as np

from Input import SpeedMS

from Method_Check import Taylor
from Method_Check import LapKeller
from Method_Check import SSPA
from Method_Check import GH
from Method_Check import S60
from Method_Check import BSRA
from Method_Check import HM
from Method_Check import Hollenbach

from Friction_Res import FrictionRes

from GH_Res import RemainingResGH
from GH_Res import TotalResGH
from GH_Res import EffectivePowerGH
from GH_Res import TotalResGHCruising
from GH_Res import EffectivePowerGHCruising

from HM_Res import CorelationResHM
from HM_Res import TransomResHM
from HM_Res import BulbResHM
from HM_Res import WaveMakingResHM
from HM_Res import AppendageResHM
from HM_Res import TotalResHM
from HM_Res import EffectivePowerHM
from HM_Res import TotalResHMCruising
from HM_Res import EffectivePowerHMCruising

from Hollenbach_Res import CorelationResHol
from Hollenbach_Res import RemainingResHol
from Hollenbach_Res import TotalResHol
from Hollenbach_Res import EffectivePowerHol
from Hollenbach_Res import TotalResHolCruising
from Hollenbach_Res import EffectivePowerHolCruising

from S60_Res import TotalResS60
from S60_Res import TotalResS60Cruising

from BSRA_Res import TotalResBSRA
from BSRA_Res import TotalResBSRACruising

from SSPA_Res import TotalResSSPA
from SSPA_Res import TotalResSSPACruising


# ======================================================================================================================
# CALCULATION OF THE AVERAGE OF THE TOTAL RESISTANCE AND EFFECTIVE POWER
# ======================================================================================================================




TotalResCruising = (TotalResGHCruising + TotalResHMCruising) / 2
#print('Total resistance at cruising speed RT =', TotalResCruising, '[kN]')


EffectivePowerCruising = (EffectivePowerGHCruising + EffectivePowerHMCruising) / 2
#print('Effective power at cruising speed PE =', EffectivePowerCruising, '[kW]')


#print('')


# ======================================================================================================================
# COMBINED RESISTANCE AND POWER GRAPHS
# ======================================================================================================================

# Hollenbach

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


# Holtrop - Mennen

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


# Guldhammer - Harvald

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


fig, axs = plt.subplots(3, 2, sharex = 'col', sharey = 'row')

axs[0, 0].plot(SpeedMS, FrictionRes, label = "Friction Resistance")
axs[0, 0].plot(SpeedMS, RemainingResGH, label = "Remaining Resistance")
axs[0, 0].plot(SpeedMS, TotalResGH, 'tab:red', label = "Total Resistance")
axs[0, 0].set_title('Guldhammer - Harvald')
plt.grid()
#plt.legend(loc="best")

axs[0, 1].plot(SpeedMS, AppendageResHM, label = "Appendage Resistance")
axs[0, 1].plot(SpeedMS, WaveMakingResHM, label = "Wawe Making Resistance")
axs[0, 1].plot(SpeedMS, BulbResHM, label = "Bulb Resistance")
axs[0, 1].plot(SpeedMS, TransomResHM, label = "Transom Resistance")
axs[0, 1].plot(SpeedMS, CorelationResHM, label = "Corelation Resistance")
axs[0, 1].plot(SpeedMS, TotalResHM, 'tab:red', label = "Total Resistance")
axs[0, 1].set_title('Holtrop - Mennen')
plt.grid()
#plt.legend(loc="best")

axs[1, 0].plot(SpeedMS, CorelationResHol, label = "Corelation Resistance")
axs[1, 0].plot(SpeedMS, FrictionRes, label = "Friction Resistance")
axs[1, 0].plot(SpeedMS, RemainingResHol, label = "Remaining Resistance")
axs[1, 0].plot(SpeedMS, TotalResHol, 'tab:red', label = "Total Resistance")
axs[1, 0].set_title('Hollenbach')
plt.grid()
#plt.legend(loc="best")

axs[1, 1].plot(SpeedMS, TotalResS60, 'tab:red')
axs[1, 1].set_title('S-60')
plt.grid()
#plt.legend(loc="best")

axs[2, 0].plot(SpeedMS, TotalResSSPA, 'tab:red')
axs[2, 0].set_title('SSPA')
plt.grid()
#plt.legend(loc="best")

axs[2, 1].plot(SpeedMS, TotalResBSRA, 'tab:red')
axs[2, 1].set_title('BSRA')
plt.grid()
#plt.legend(loc="best")








for ax in axs.flat:
    ax.set(xlabel='Speed [m/s]', ylabel='Resistance [kN]')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

plt.show()












