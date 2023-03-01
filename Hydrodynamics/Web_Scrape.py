# Web scrape script
import datetime
import pandas as pd
import wget

test_date = datetime.datetime.strptime("20201217", "%Y%m%d")
Nb_days = 680

date_generated = pd.date_range(test_date, periods=Nb_days)

for i in range(len(date_generated.strftime("%Y%m%d"))):
    break
    url = "https://rwsprojectarchief.openearth.nl/downloads/houtribdijk/data_tailored/STB/FL66/" + 'STB_FL66_' + date_generated.strftime("%Y%m%d")[i] + '000000.nc'
    wget.download(url, '/home/casper/Documents/Aardwetenschappen/Marker Wadden/STB_FL66/')
