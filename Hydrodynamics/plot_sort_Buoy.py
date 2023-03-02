import os
import netCDF4
import xarray
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime


def SortByDay(path_of_dir):
    
    for files in os.listdir(path_of_dir):
        if files.endswith('.nc'):
            old_dir = path_of_dir + files
            if os.path.isdir(path_of_dir + files[10:18]):
                new_dir = path_of_dir + files[10:18] + '/' + files
                os.rename(old_dir, new_dir)
            else:
                os.mkdir(path_of_dir + files[10:18])
                new_dir = path_of_dir + files[10:18] + '/' + files
                os.rename(old_dir, new_dir)
        else:
            continue


def Average_15min(path_of_dir):
    meanlst = []
    timelst = []
    for files in sorted(os.listdir(path_of_dir)):
        if files.endswith('.nc'):
            ds = netCDF4.Dataset(path_of_dir + files, 'r')
            WH = np.array(ds['WATHTE'][:])

        if len(WH) == 14400:
            for i in [0, 3600, 7200, 10800]:
                meanlst.append(np.nanmean(WH[i:i+3600]))
        else:
            print(files)

        time_since = datetime.datetime(int(files[10:14]), int(files[14:16]), int(files[16:18])) - datetime.datetime(1970, 1, 1)  
    seconds = int(time_since.total_seconds())*1000
    for i in range(len(meanlst)):
        timelst.append((seconds + i*900000))
        
    return meanlst, timelst



if __name__ == '__main__':
    
    Sort_needed = False; Avg_data_needed = False

    if Sort_needed:
        SortByDay('/home/casper/Documents/Aardwetenschappen/Marker Wadden/Waterhoogtes/ADV/2021/')

    if Avg_data_needed:
        for files in sorted(os.listdir('/home/casper/Documents/Aardwetenschappen/Marker Wadden/Waterhoogtes/ADV/2021/')):
            folder_path = ('/home/casper/Documents/Aardwetenschappen/Marker Wadden/Waterhoogtes/ADV/2021/' + files + '/')
            meanlst, timelst = Average_15min(folder_path)

            dict = {'time (ms)': timelst, 'mean water level (m)': meanlst}
            df = pd.DataFrame(dict)
            df.to_csv('/home/casper/Documents/Aardwetenschappen/Marker Wadden/Waterhoogtes/ADV/2021/csv/'+ files + '.csv')

        
        path = '/home/casper/Documents/Aardwetenschappen/Marker Wadden/Waterhoogtes/ADV/2021/csv/'
        csv_list = []
        file_list = [path + f for f in os.listdir(path)]
        for file in sorted(file_list):
            csv_list.append(pd.read_csv(file))
        csv_merged = pd.concat(csv_list, ignore_index=True)
        csv_merged.to_csv(path + '2021.csv', index=False)



    data = np.array(pd.read_csv('Hydrodynamic_Data/ADV_BUOY1_All.csv'))
    time = data[:,0]
    Waterheight = np.where((data[:,1]>1) | (data[:,1]<-0.5), np.nan, data[:,1])

    plt.scatter(time, Waterheight, s=1); 
    plt.ylabel('Mean water level [m NAP]')
    plt.show()
