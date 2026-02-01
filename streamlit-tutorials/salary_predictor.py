import streamlit as st
import pandas as pd
from matplotlib import pyplot as plt
from plotly import graph_objs as go
from sklearn.linear_model import LinearRegression
import numpy as np

data = pd.read_csv('Salary_Data.csv')
x = np.array(data['YearsExperience']).reshape(-1,1)
linear_regression = LinearRegression()
linear_regression.fit(x,np.array(data['Salary']))

st.title('Salary Predictor')
st.image("salary.jpg",width = 650)
nav = st.sidebar.radio("Links",["Home","Prediction","Contribute"])

if nav == "Home":
   if st.checkbox("Show Table"):
        st.table(data)
        
   graph = st.selectbox("What kind of graph?", ["Interactive", "Non-Interactive"])
   value = st.slider("Filter data using years",0,10)
   data = data.loc[data["YearsExperience"] >= value]
   if graph == "Non-Interactive":
      plt.figure(figsize = (10, 5))
      plt.scatter(data["YearsExperience"], data["Salary"])
      plt.ylim(0)
      plt.xlabel("Years of Experience")
      plt.ylabel("Salary")
      plt.tight_layout()
      st.pyplot()
      
   if graph == "Interactive":
        layout =go.Layout(
            xaxis = dict(range=[0,16]),
            yaxis = dict(range =[0,210000])
        )
        fig = go.Figure(data=go.Scatter(x=data["YearsExperience"], y=data["Salary"], mode='markers'),layout = layout)
        st.plotly_chart(fig)

