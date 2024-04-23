# import module
import streamlit as st
import pandas as pd
import numpy as np

# membuat data
# data array
a = np.array([1,2,3,4])
b = np.array([(1.2, 2.3, 2.6),(3.5, 4.1, 7.2)], dtype = float)

# membuat tipe data series
u = pd.Series([1,2,3,4,5,6,7])

# ambil dataset dari github
dataset = pd.read_csv("https://raw.githubusercontent.com/jumadi-cloud/Fundamental-Python/main/Dataset/datagaji1.csv")

# membuat data dictionary
profil = {
    'Nama':'Ucup',
    'Umur':'21',

    'Pemrograman': ['Python', 'NodeJS'],

    'Favorit': {
        'Makanan':'Indomie',
        'Hobi':'Rebahan'
    }
}

# cara menampilkan data
# dataframe
st.text("Ini adalah dataframe:")
st.dataframe(b)
st.dataframe(u)
st.dataframe(dataset)

# tabel
st.text("Ini adalah tabel:")
st.table(a)
st.table(dataset)

# json
st.text("Ini adalah tipe data json:")
st.json(profil)

# metric
st.text("Ini adalah metric:")
st.text("Contoh 1:")


st.metric(label="Gas price", value=4, delta=-0.5,
    delta_color="inverse")

st.metric(label="Active developers", value=123, delta=123,
    delta_color="off")

st.text("Contoh 2:")

col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")