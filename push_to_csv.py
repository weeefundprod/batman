import csv
import pandas as pd
from get_value_of_variantes import *

print("push to csv")

# csv_file = open("weefundinventory.csv", "w")

# with open('weeefundInventory.csv','a') as fd:
#     fd.write(str(serial_number, product))

data = [(serial_number,product,sku,vendor,screen,ram,hhdssd,graphic_card,webcam,bluetooth,dvd)]
df = pd.DataFrame(data)

# if file exists....
if os.path.isfile('weeefundInventory.csv'):
    #Old data
    oldFrame = pd.read_csv('weeefundInventory.csv')
    #oldFrame.columns = oldFrame.iloc[0]
    #print(oldFrame.columns)

    #Concat
    df_diff = pd.concat([oldFrame, df],ignore_index=True).drop_duplicates()

    #Write new rows to csv file
    df_diff.to_csv('weeefundInventory.csv', header=False, index=False)

else: # else it exists so append
    df.to_csv('weeefundInventory.csv', header=False, index=False)