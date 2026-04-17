import streamlit as st
import pandas as pd

def load_data():
    df = pd.read_csv("dataset\covid_19_indonesia_time_series_all.csv")
    return df

def show_data():
    df = load_data()
    st.subheader("Data Covid-19 Indonesia")
    df_filtered = df[[
        "Location",
        "New Cases",
        "New Deaths",
        "New Recovered",
        "Total Cases",
        "Total Deaths",
        "Total Recovered"
    ]]
    
    st.dataframe(df_filtered.head(10))

    total_kasus = df["Total Cases"].sum()
    st.write("Total Kasus Keseluruhan:", int(total_kasus))

    st.subheader("Statistik Deskriptif Dataset")
    st.write(df.describe())
