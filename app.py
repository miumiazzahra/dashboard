import streamlit as st
from data import *

#judul dashboard
def judul():
    st.title("Dashboard Covid-19")
    st.write("Selamat data di Dashboard Covid-19. Di sini Anda dapat melihat data terbaru tentang Covid-19 di Indonesia")

st.sidebar.title("Navigasi")
menu = st.sidebar.radio("Pilih Halaman", ["Home", "Halaman Data"])

if menu == "Home":
    judul()
    df = load_data()
    year = select_year()
    location = select_location(df)
    df_filtered = filter_data(df, year, location)

    kolom(df_filtered)
    pie_chart1(df_filtered)
    bar_chart1(df_filtered)
    bar_chart2(df_filtered)
    map_chart(df_filtered, year)

elif menu == "Halaman Data":
    judul()
    df = load_data()
    year = select_year()
    location = select_location(df)
    df_filtered = filter_data(df, year, location)

    show_data(df_filtered)

st.markdown("---")
st.caption("© Umi Qusnul AG - 184240024")