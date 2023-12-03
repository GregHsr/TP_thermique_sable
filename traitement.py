import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Importation des données
data = pd.read_csv("TPsable_partie1.csv", sep=",", header=0)

"""data.iloc[:, 0]
;  Fichier de donn�es.*** Acquisition T� pour mesure de conductivit�. ***
;  Mesure enregistr�e le : 27/11/2023 � 16:00:56
;
;  Fr�quence acquisition : 2 S/s .
;  Courant de chauffage (en A):
 1.50000000000000E+0000
;  R�sistance �lectrique lin�aire de l'�l�ment chauffant (Ohms/m):
 9.10000038146973E+0000
;  Liste des canaux:
CH0	CH1	CH2	CH3	CH4	CH5	CH6
;  Positions des curseurs de mesure:
0.5	0.5	0.5	0.5	0.5	0.5	0.5
4803	4803	4803	4803	4803	4803	4803
;  Donn�es Temp�rature (�C) :
"""

plt.figure(1)
for channel in range(7):
    plt.plot([0.5*k for k in range(len(data.iloc[:, channel]))],data.iloc[:, channel], label=data.columns[channel])
plt.xlabel('Temps [s]')
plt.ylabel('Température [°C]')
plt.legend()

index_refroi = int(2444 *2)
plt.figure(2)
channel = 0
plt.plot([np.log(0.5*k) for k in range(1500,index_refroi)],data.iloc[1500:index_refroi, channel], label=data.columns[channel])
plt.xlabel('Temps Logarithmique')
plt.ylabel('Température [°C]')
plt.show()

# Régression linéaire avec numpy

a, b = np.polyfit([np.log(0.5*k) for k in range(1500,index_refroi)],data.iloc[1500:index_refroi, channel], 1)
print(a, b)