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
    year = select_year()
    df = load_data()
    df_filtered = filter_data(df, year)
    kolom(df_filtered)
    pie_chart1(df_filtered)
elif menu == "Halaman Data":
    judul()
    year = select_year()
    df = load_data()
    df_filtered = filter_data(df, year)
    show_data(df_filtered)

st.markdown("---")
st.caption("© Umi Qusnul AG - 184240024")