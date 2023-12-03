import numpy as np
import matplotlib.pyplot as plt

# Lecture des données

"""
Vendor,GRAPHTEC Corporation
Model,GL820
Version,Ver1.12
Sampling,200ms
Total data points,57736       
Start time,2023-11-27,14:08:41
End time,2023-11-27,17:21:09
Trigger time,2023-11-27,14:08:42
AMP Settings
CH,Signal name,Input,Range,Filter,Span
CH1, " CH 1",TEMP,TC_K,5,70.000000,20.000000,degC
CH2, " CH 2",TEMP,TC_K,5,70.000000,20.000000,degC
CH3, " CH 3",TEMP,TC_K,5,70.000000,20.000000,degC
CH4, " CH 4",TEMP,TC_K,5,70.000000,20.000000,degC
CH5, " CH 5",TEMP,TC_K,5,70.000000,20.000000,degC
CH6, " CH 6",TEMP,TC_K,5,70.000000,20.000000,degC
CH8, " CH 8",TEMP,TC_K,5,70.000000,20.000000,degC
CH9, " CH 9",TEMP,TC_K,5,70.000000,20.000000,degC
CH10, " CH10",TEMP,TC_K,5,70.000000,20.000000,degC
CH11, " CH11",TEMP,TC_K,5,70.000000,20.000000,degC
CH12, " CH12",TEMP,TC_K,5,70.000000,20.000000,degC
CH13, " CH13",TEMP,TC_K,5,70.000000,20.000000,degC
CH14, " CH14",TEMP,TC_K,5,70.000000,20.000000,degC
CH15, " CH15",TEMP,TC_K,5,70.000000,20.000000,degC
CH20, " CH20",TEMP,TC_K,5,70.000000,20.000000,degC
Logic/Pulse,Off
Data
Number,Date&Time,ms,CH1,CH2,CH3,CH4,CH5,CH6,CH8,CH9,CH10,CH11,CH12,CH13,CH14,CH15,CH20,Alarm1-10,Alarm11-20,AlarmOut
NO.,Time,ms,degC,degC,degC,degC,degC,degC,degC,degC,degC,degC,degC,degC,degC,degC,degC,A1234567890,A1234567890,A1234
"""

# Data

Number = []
Date = []
ms = [] 
CH1 = []
CH2 = []
CH3 = []
CH4 = []
CH5 = []
CH6 = []
CH8 = []
CH9 = []
CH10 = []
CH11 = []
CH12 = []
CH13 = []
CH14 = []
CH15 = []
CH20 = []
Alarm1 = []
Alarm11 = []
AlarmOut = []

data = open("TPsable_partie2.csv", "r")
data.readline()
for line in data:
    line = line.split(",")
    Number.append(int(line[0]))
    CH1.append(float(line[3]))
    CH2.append(float(line[4]))
    CH3.append(float(line[5]))
    CH4.append(float(line[6]))
    CH5.append(float(line[7]))
    CH6.append(float(line[8]))
    CH8.append(float(line[9]))
    CH9.append(float(line[10]))
    CH10.append(float(line[11]))
    CH11.append(float(line[12]))
    CH12.append(float(line[13]))
    CH13.append(float(line[14]))
    CH14.append(float(line[15]))
    CH15.append(float(line[16]))
    CH20.append(float(line[17]))

# Plot

plt.figure(0)
plt.plot(CH1, label="CH1")
plt.plot(CH2, label="CH2")
plt.plot(CH3, label="CH3")
plt.plot(CH4, label="CH4")
plt.plot(CH5, label="CH5")
plt.plot(CH6, label="CH6")
plt.plot(CH8, label="CH8")
plt.plot(CH9, label="CH9")
plt.plot(CH10, label="CH10")
plt.plot(CH11, label="CH11")
plt.plot(CH12, label="CH12")
plt.plot(CH13, label="CH13")
plt.plot(CH14, label="CH14")
plt.plot(CH15, label="CH15")
plt.plot(CH20, label="CH20")
plt.legend()

plt.show()


#FFT : np.fft.fft(n=)