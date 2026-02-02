import streamlit as st
import pandas as pd
import numpy as np
import time
import matplotlib.pyplot as plt
import altair as alt

# Basic of Stremlit

st.title("Welcome to the world of streamlit programming")
st.header("This is a header section")
st.subheader("This is a sub header section")
st.text("This is a sample text")

# Working with datasets
a = [1,2,3,4,5,6,7,8]
b = [11,12,13,14,15,16,17,18]
n = np.array(a)
nd = n.reshape((2,4))

# Sample dictionary
dic = {
    "name": "Keerthi Kumar N",
    "age": 40,
    "city": "India"
}

data = pd.read_csv("stock.csv")
df = pd.DataFrame(np.random.randn(100,3), columns=['a','b','c'])

st.dataframe(a);
st.json(dic)
st.write(nd)

# Charts and plots
st.line_chart(df)
st.bar_chart(df)
st.area_chart(df)

# altair_chart
chart = alt.Chart(df).mark_circle().encode(x = 'a', y = 'b',tooltip = ['a','b'])
st.altair_chart(chart, use_container_width=True)

# media 
st.image("ak icon.jpg", width=300)
st.video("https://youtu.be/5XnHlluw-Eo")  
