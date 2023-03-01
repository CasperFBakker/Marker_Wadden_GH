import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from Classes.SetupQuestions import *

WindData = np.array(pd.read_csv('/home/casper/Documents/Aardwetenschappen/Marker Wadden/CoastSat_PlanetScope_MarkerWadden/Hydrodynamic_Data/WindData_Houtribdijk.csv'))
WindKracht_Dic = {"0 Bft": 0, "1 Bft": 0.3, "2 Bft": 1.6, "3 Bft": 3.4, "4 Bft": 5.5, "5 Bft": 8, "6 Bft":10.8, "7 Bft": 13.9, "8 Bft":17.2, "9 Bft": 20.8}

WindSpeed = SetupQuestions.Q_Filter_WindSpeed(WindKracht_Dic)

plt.subplot(2,1,1)
date = np.arange(0, len(WindData))
Beaufort_min = np.array([0, 0.3, 1.6, 3.4, 5.5, 8, 10.8, 13.9, 17.2, 20.8])
Beaufort_max = np.array([0.2, 1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4])
BeaufortColors = ['dodgerblue', 'cyan', 'turquoise', 'limegreen', 'palegreen', 'yellowgreen', 'lightyellow', 'khaki', 'gold', 'goldenrod']
BeaufortLabel = ['Windkracht 0 bft', 'Windkracht 1 bft', 'Windkracht 2 bft', 'Windkracht 3 bft', 'Windkracht 4 bft', 
                 'Windkracht 5 bft', 'Windkracht 6 bft', 'Windkracht 7 bft',  'Windkracht 8 bft', 'Windkracht 9 bft']
plt.scatter(np.where((WindData[:,4]/10)>WindSpeed, date, np.nan), np.where((WindData[:,4]/10)>WindSpeed, (WindData[:,4]/10), np.nan))

for i in range(len(Beaufort_min)):
    plt.vlines(-40, Beaufort_min[i], Beaufort_max[i], colors=BeaufortColors[i], label=BeaufortLabel[i])
    for j in range(20):
        plt.vlines(-40+j, Beaufort_min[i], Beaufort_max[i], colors=BeaufortColors[i])
plt.xticks([0, 366, 732, 1099, 1464, 1830], ['2018', '2019', '2020', '2021', '2022', '2023'])
plt.xlim([-40, 1900]); plt.ylim([0, 24.4])
plt.legend()
plt.ylabel('Windsnelheid (m/s)')

plt.subplot(2,1,2)
plt.yticks([0, 45, 90, 135, 180, 225, 270, 315, 360],['N', 'NO', 'O',  'ZO', 'Z', 'ZW', 'W',  'NW', 'N'])

plt.scatter(np.where((WindData[:,4]/10)>WindSpeed, date, np.nan), np.where((WindData[:,4]/10)>WindSpeed, (WindData[:,3]), np.nan))

plt.xticks([0, 366, 732, 1099, 1464, 1830], ['2018', '2019', '2020', '2021', '2022', '2023'])
plt.xlim([-40, 1900]); plt.ylim([-10, 370])
plt.ylabel('Windrichting')



Windkracht_Data = (WindData[:,4]/10)
WindRichting_Data = WindData[:,3]
Wind_Datum = WindData[:,2]
WindKracht_Filt = Windkracht_Data[Windkracht_Data >WindSpeed] 
WindRichting_Filt = WindRichting_Data[Windkracht_Data>WindSpeed] 
Wind_Datum_Filt = Wind_Datum[Windkracht_Data >WindSpeed]


Data_Arr = np.array([Wind_Datum_Filt, WindKracht_Filt, WindRichting_Filt]).T
DF = pd.DataFrame(Data_Arr)
DF.to_csv('Filtered_WindData.csv', header=['Datum', 'Windsnelheid (m/s)', 'Windrichting (graden)'], index=False)


# WaterHoogte = np.array(pd.read_csv('Hydrodynamic_Data/WaterHoogte_MarkMeer_18_19.csv'))[:,6]
# np.append(WaterHoogte, np.zeros((len(date)-len(WaterHoogte),1)))

# print(len(WaterHoogte))
# print(len(date))
# plt.subplot(3,1,3)
# plt.scatter(date, WaterHoogte) 




plt.show()












