import netCDF4
import xarray
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file2read = netCDF4.Dataset('Hydrodynamic_Data/STB_FL65_All.nc', 'r') 
var = file2read.variables['GEM_WATHTE']
Hm0 = file2read.variables['Hm0']
t1 = file2read.variables['time']

file2read = netCDF4.Dataset('Hydrodynamic_Data/STB_FL66_All.nc', 'r') 
var2 = file2read.variables['GEM_WATHTE']
Hm02 = file2read.variables['Hm0']
t2 = file2read.variables['time']

plt.subplot(4,1,1)
plt.scatter(t1[:], var[:], s=1, label='STB_FL65 (ZS)')
plt.scatter(t2[:], var2[:], s=1, label='STB_FL66 (NS)')
plt.ylabel('Waterhoogte [m NAP]', fontsize=14)
plt.xticks([1554076800000, 1556668800000, 1559347200000, 1561939200000, 1564617600000, 1567296000000, 1569888000000, 1572566400000, 1575158400000, 
            1577836800000, 1580515200000, 1583020800000, 1585699200000, 1588291200000, 1590969600000, 1593561600000, 1596240000000, 1598918400000,
            1601510400000, 1604188800000, 1606780800000, 1609459200000, 1612137600000], 
           [ " " , " " , " " , " ",  " " , " ", " ", " " , " ", " ", " ", " ", " ", " " ," ", " ", " ", " ", " ", " " , " ",  " ", " "])
plt.legend()
WindData_Uur = np.array(pd.read_csv('Hydrodynamic_Data/WindData_Uur_Houtribdijk_Period.csv'))
WindDirection = WindData_Uur[:,3]
WindDirectionFilt = np.where(WindDirection==990, np.nan, WindDirection)

plt.subplot(4,1,2)
plt.scatter(WindData_Uur[:,0], WindData_Uur[:,4]/10,s=1.75)
plt.ylabel('Windsnelheid [m/s]', fontsize=14)
plt.xticks([1554076800000, 1556668800000, 1559347200000, 1561939200000, 1564617600000, 1567296000000, 1569888000000, 1572566400000, 1575158400000, 
            1577836800000, 1580515200000, 1583020800000, 1585699200000, 1588291200000, 1590969600000, 1593561600000, 1596240000000, 1598918400000,
            1601510400000, 1604188800000, 1606780800000, 1609459200000, 1612137600000], 
           [ " " , " " , " " , " ",  " " , " ", " ", " " , " ", " ", " ", " ", " ", " " ," ", " ", " ", " ", " ", " " , " ",  " ", " "])

plt.subplot(4,1,3)
plt.scatter(WindData_Uur[:,0], WindDirectionFilt,s=1.75)
plt.ylabel('Windrichting  [$^\circ$]', fontsize=14)
plt.xticks([1554076800000, 1556668800000, 1559347200000, 1561939200000, 1564617600000, 1567296000000, 1569888000000, 1572566400000, 1575158400000, 
            1577836800000, 1580515200000, 1583020800000, 1585699200000, 1588291200000, 1590969600000, 1593561600000, 1596240000000, 1598918400000,
            1601510400000, 1604188800000, 1606780800000, 1609459200000, 1612137600000], 
           [ " " , " " , " " , " ",  " " , " ", " ", " " , " ", " ", " ", " ", " ", " " ," ", " ", " ", " ", " ", " " , " ",  " ", " "])

plt.subplot(4,1,4)
plt.plot(t1[:], Hm0[:], label='STB_FL65 (ZS)')
plt.plot(t2[:], Hm02[:], label='STB_FL66 (NS)')
plt.ylabel('Hm0 [m]', fontsize=16)
plt.xticks([1554076800000, 1556668800000, 1559347200000, 1561939200000, 1564617600000, 1567296000000, 1569888000000, 1572566400000, 1575158400000, 
            1577836800000, 1580515200000, 1583020800000, 1585699200000, 1588291200000, 1590969600000, 1593561600000, 1596240000000, 1598918400000,
            1601510400000, 1604188800000, 1606780800000, 1609459200000, 1612137600000], 
           ["April '19", " " ,"Juni '19", " ", "Augustus '19", " ", "Oktober '19", " " , "December '19", " ", "Februari '20", " ", "April '20", 
            " " ,"Juni '20", " ", "Augustus '20", " ", "Oktober '20", " " , "December '20",  " ", "Februari '21"], fontsize=14)
plt.legend(loc=1)
plt.show()



# file2read = netCDF4.Dataset('Hydrodynamic_Data/STB_FL65/STB_FL65_20190330000000.nc', 'r') 
# print(file2read.variables.keys())
# ds = xarray.open_mfdataset('Hydrodynamic_Data/ADV/New Folder/*.nc')
# ds.to_netcdf('Hydrodynamic_Data/ADV_BUOY1_All_1.nc')