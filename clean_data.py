import pandas as pd
import glob
import matplotlib.pyplot as plt
import numpy as np
%matplotlib notebook
import requests
import json
#download the top 3 crimes CSV files
#use glob to find all CSV files in a directory
all_files = glob.glob("*csv")
#create an empty list to store DataFrames
df_list =[]
#loop through each file and read it into a DataFrame
for file in all_files:
    df = pd.read_csv(file)
    df_list.append(df)
#concatenate the list of DataFrames into a single DataFrame
result = pd.concat(df_list, axis=0, ignore_index=True)
#find the columns names
result.columns
crimes = result["premises_type"].value_counts()
# Use DataFrame.plot() in order to create a bar chart of the data
crimes.plot(kind="bar", figsize=(10, 5))
# Set a title for the chart
plt.title("Discover where the crimes are happening in Toronto")
plt.show()
plt.tight_layout()