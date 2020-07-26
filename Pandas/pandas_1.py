import pandas as pd


# Return Dataframe df
df = pd.read_csv(
    '/Users/abhishek.panda/Documents/My/ML_in_Python/data/weather_data_nyc_centralpark_2016.csv')


# Max temp
print(df['Temperature'].max())

print(df['EST'][df['Events'] == 'Snow'])
