import numpy as np
import pandas as pd
arr = [2,3,4,4,3,4,5,6,7,7,7,8,9,7,7,7,7,6,5,4,3,2,3,4,4,3,4,5,6,7,7,7,8,9,7,7,7,7,6,5,4,3,3,4,5,6,6,7,8,8,3,3,4,5,6,7,8,9,7,5,4,2,1]

"Total storm days of whole period:"

# treshold = 5
# lst = []
# for i in range(len(arr)):

#     if arr[i] > treshold: 
#         lst.append(arr[i])
#         print(len(lst))
#     else:
#         pass


# "Days per storm event:"

# treshold = 5
# lst = []
# for i in range(len(arr)):

#     if arr[i] > treshold: 
#         if arr[i+1] > treshold: 
#             lst.append(arr[i])
#         else:
#             print(len(lst)+1)
#             lst = []
#     else:
#         pass



def Duration_StormEvents(arr, treshold):
    
    lst = []
    final = []
    Final_Arr = np.array(final)
    for index, value in enumerate(arr):
        if index < len(arr)-1:
            if value > treshold: 
                if arr[index+1] > treshold: 
                    lst.append(value)
                else:
                    lst.append(value)
                    new_arr = np.array([len(lst), np.mean(lst), np.max(lst)])
                    Final_Arr = np.hstack((Final_Arr, new_arr))
                    lst = []
        else:
            pass
    Final_Arr = np.reshape(Final_Arr, (int(len(Final_Arr)/3), 3))

    return Final_Arr


def Total_NbStormHours():
    pass

arr = [2,3,4,4,3,4,5,6,7,7,7,8,9,7,7,7,7,6,5,4,3,2,3,4,4,3,4,5,6,7,7,7,8,9,7,7,7,7,6,5,4,3,3,4,5,6,6,7,8,8,3,3,4,5,6,7,8,9,7,5,4,2,1]

WindData_Uur = np.array(pd.read_csv('/home/casper/Documents/Aardwetenschappen/Marker Wadden/CoastSat_PlanetScope_MarkerWadden/Hydrodynamic_Data/WindData_Uur_Houtribdijk.csv'))
arr = WindData_Uur[:,4]/10

print(Duration_StormEvents(arr, 20.8))

print(np.shape(Duration_StormEvents(arr, 20.8)))

print(len(arr))