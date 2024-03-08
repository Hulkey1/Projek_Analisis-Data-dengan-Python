import pandas as pd
import matplotlib.pyplot as mlpl
import seaborn as sr
import streamlit as sl

day_df = pd.read_csv("https://raw.githubusercontent.com/Hulkey1/Projek_Analisis-Data-dengan-Python/main/Dataset/day.csv")
print(day_df.head())

hour_df = pd.read_csv("https://raw.githubusercontent.com/Hulkey1/Projek_Analisis-Data-dengan-Python/main/Dataset/hour.csv")
print(hour_df.head())

if 'hour_df' in locals():
    del hour_df
    print("Variabel 'hour_df' telah dihapus.")

drop_col = ['instant', 'weathersit', 'temp', 'atemp', 'hum', 'windspeed']

for i in day_df.columns:
    if i in drop_col:
        day_df.drop(labels=i, axis=1, inplace=True)

categorical_cols = ['season', 'yr', 'mnth', 'holiday', 'weekday', 'workingday']

for col in categorical_cols:
    fig = px.bar(day_df[col].value_counts().reset_index(), x='index', y=col)
    fig.update_layout(title=f'Distribusi {col}')
    fig.show()
  
#Jumlah penyewaan sepeda pada tahun 2011
total_sewa_sepeda = day_df[day_df["yr"] == 0]["cnt"].sum()

#Jumlah penyewaan sepeda pada tahun 2012
total_sewa_sepeda = day_df[day_df["yr"] == 1]["cnt"].sum()

# Jumlah total sewa sepeda tahun 2012 selama musim semi
filtered_data = day_df[(day_df["yr"] == 1) & (day_df["season"] == 1)]
total_sewa_sepeda = filtered_data["cnt"].sum()

# Jumlah total sewa sepeda tahun 2012 selama musim panas
filtered_data = day_df[(day_df["yr"] == 1) & (day_df["season"] == 2)]
total_sewa_sepeda = filtered_data["cnt"].sum()

# Jumlah total sewa sepeda tahun 2012 selama musim panas
filtered_data = day_df[(day_df["yr"] == 1) & (day_df["season"] == 3)]
total_sewa_sepeda = filtered_data["cnt"].sum()

# Jumlah total sewa sepeda tahun 2012 selama musim dingin
filtered_data = day_df[(day_df["yr"] == 1) & (day_df["season"] == 4)]
total_sewa_sepeda = filtered_data["cnt"].sum()
