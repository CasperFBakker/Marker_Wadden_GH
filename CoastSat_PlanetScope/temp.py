# import numpy as np
# import pandas as pd
# # ps_data = copy.deepcopy(sl_csv[['Date',transect]])
# ps_data = pd.read_csv('/home/casper/Documents/Aardwetenschappen/Marker_Wadden/Marker_Wadden_GH/CoastSat_PlanetScope/outputs/MarkerWadden_Test/shoreline outputs/Local Coreg/NmB/Peak Fraction/MarkerWadden_Test_NmB_Peak Fraction_transect_SL_data_tide_corr.csv')
# ps_data.loc[:,'Date'] = pd.to_datetime(ps_data.loc[:,'Date'], utc = True)
# ps_data = ps_data.set_index('Date')
# # ps_data = ps_data[np.isfinite(ps_data[transect])]
# print(ps_data)
# print((max(ps_data.index)-min(ps_data.index)).days)


import pickle
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
with open('/home/casper/Documents/Aardwetenschappen/Marker_Wadden/Marker_Wadden_GH/CoastSat_PlanetScope/outputs/MarkerWadden_Test/shoreline outputs/Local Coreg/NmB/Peak Fraction/MarkerWadden_Test_NmB_Peak Fraction_shorelines.pkl', 'rb') as f:
    data = pickle.load(f)

print(data["shorelines"])
sl = data["shorelines"]
sl = np.array(sl[1])
print(type(sl))
print(np.size(sl))

x = []; y = []
for i in range(len(sl)):
    temp = sl[i]
    x.append(temp[0])
    y.append(temp[1])

x = pd.Series(x)    
y = pd.Series(y)

x.to_csv('x.csv')
y.to_csv('y.csv')
# sl = np.array([sl])
# print(np.size(sl))



# kl = pd.Series(sl)
# kl.to_csv('test.csv')
# # print(np.shape(sl))

# sl = np.vstack(sl)

# plt.imshow(sl)
# plt.xlim([152271, 155500])
# plt.ylim([508141, 510000])
# plt.show()