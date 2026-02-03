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

# Widgets - buttons
if st.button("Click me"):
    st.text("You clicked me")

# 2.Textinput
name = st.text_input("Name")
st.write(name)

# 3.textarea
address = st.text_area("Address")
st.write(address)

# 4. date and time
st.date_input("Date")
st.time_input("Time")

# 5. checkbox
if st.checkbox("Show dataframe"):
    st.write("Thanks for checking the dataframe part")

# 6. radio
st.radio("Choose a number", ("1","2","3"))

# 7. selectbox
st.selectbox("Select a number", ("1","2","3"))

# 8.multiselect
v3 = st.multiselect("Select a number", ("1","2","3"))
st.write(v3)

# 9.slider
st.slider("Select a number", 1, 10)

# 10.number_input
st.number_input("Select a number", 1, 10)

# 11.upload_file
img = st.file_uploader("Upload a file")
#st.image(img)

# 12.progress
progress = st.progress(0)
for i in range(100):
    time.sleep(0.1)
    progress.progress(i+1)

# 13.sidebar
#st.sidebar.selectbox("Select a number", [1,2,3,4,5])

# 14. navigation bar
rad = st.sidebar.radio("Navigation", ("Home", "About", "Careers", "Contact"))
if rad == "About":
    st.write("This is about us")
if rad == "Careers":
    st.write("You clicked on the careers page.")
