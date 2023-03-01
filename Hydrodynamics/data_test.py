import netCDF4
import matplotlib.pyplot as plt
import os 
import numpy as np
import time
lst = []
# start = time.time()

# path_of_the_directory = 'Hydrodynamic_Data/ADV/'
# for filename in sorted(os.listdir(path_of_the_directory)):
#     f = os.path.join(path_of_the_directory,filename)
#     if os.path.isfile(f):
#         print(f)
#         file2read = netCDF4.Dataset(f, 'r') 
#         var = file2read.variables['WATHTE'][:]
#         lst.append(np.nanmean(var))

# end = time.time()

# print('Run: ', (end-start), 's')


# plt.scatter(np.arange(0,len(lst)), lst)
# plt.show()


# file2read = netCDF4.Dataset('Hydrodynamic_Data/ADV/ADV_BUOY1_20210330120000.nc', 'r') 
# print(file2read.variables.keys())
# print(file2read.variables['latitude'][:], file2read.variables['longitude'][:])
# var = file2read.variables['WATHTE']
# print(var)



# print(file2read.variables['GEM_WATHTE'])

 

# # Web scrape script
# import datetime
# import pandas as pd
# import wget

# test_date = datetime.datetime.strptime("20201217", "%Y%m%d")
# Nb_days = 680

# date_generated = pd.date_range(test_date, periods=Nb_days)

# for i in range(len(date_generated.strftime("%Y%m%d"))):
#     break
#     url = "https://rwsprojectarchief.openearth.nl/downloads/houtribdijk/data_tailored/STB/FL66/" + 'STB_FL66_' + date_generated.strftime("%Y%m%d")[i] + '000000.nc'
#     wget.download(url, '/home/casper/Documents/Aardwetenschappen/Marker Wadden/STB_FL66/')




# file2read = netCDF4.Dataset('Hydrodynamic_Data/STB_FL65/STB_FL65_20190330000000.nc', 'r') 
# print(file2read.variables.keys())
# var = file2read.variables['Hm0']
# print(var)
import xarray
import pandas as pd
import matplotlib.pyplot as plt
# ds = xarray.open_mfdataset('Hydrodynamic_Data/ADV/New Folder/*.nc')
# ds.to_netcdf('Hydrodynamic_Data/ADV_BUOY1_All_1.nc')

# file2read = netCDF4.Dataset('Hydrodynamic_Data/ADV/ADV_BUOY1_20190918000000.nc', 'r') 
# print(file2read.variables.keys())
# Z_var = file2read.variables['time']
# print(Z_var)
# # for i in range(len(Z_var)):
# #     print(Z_var[i])

file2read = netCDF4.Dataset('Hydrodynamic_Data/STB_FL65_All.nc', 'r') 
var = file2read.variables['GEM_WATHTE']
Hm0 = file2read.variables['Hm0']
t1 = file2read.variables['time']

file2read = netCDF4.Dataset('Hydrodynamic_Data/STB_FL66_All.nc', 'r') 
var2 = file2read.variables['GEM_WATHTE']
t2 = file2read.variables['time']

plt.subplot(4,1,1)
plt.scatter(t1[:], var[:], s=1)
plt.scatter(t2[:], var2[:], s=1)
plt.ylabel('Mean water level [m NAP]')

WindData_Uur = np.array(pd.read_csv('Hydrodynamic_Data/WindData_Uur_Houtribdijk_Period.csv'))
WindDirection = WindData_Uur[:,3]
WindDirectionFilt = []
for index, value in enumerate(WindDirection):
    if value !=990:
        WindDirectionFilt.append(value)
    else: 
        WindDirectionFilt.append(np.nan)
plt.subplot(4,1,2)
plt.plot(WindData_Uur[:,0], WindData_Uur[:,4]/10)
plt.ylabel('Mean wind speed [m/s]')

plt.subplot(4,1,3)
plt.plot(WindData_Uur[:,0], WindDirectionFilt)
plt.ylabel('Mean wind direction  [$^\circ$]')

plt.subplot(4,1,4)
plt.plot(t1[:], Hm0[:])
plt.ylabel('Hm0 [m]')

plt.show()

