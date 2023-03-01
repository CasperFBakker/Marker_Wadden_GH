# importing panda library
import pandas as pd

# readinag given csv file
# and creating dataframe
dataframe1 = pd.read_csv("/home/casper/Documents/Aardwetenschappen/Marker Wadden/uurgeg_258_2021-2030.txt")

# storing this dataframe in a csv file
dataframe1.to_csv('/home/casper/Documents/Aardwetenschappen/Marker Wadden/uurgeg_258_2021-2030.csv', index = None)