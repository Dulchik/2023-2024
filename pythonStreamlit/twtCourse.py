import streamlit as st
import pandas as pd
import numpy as np
import matplotlib as plt

st.title("Streamlit Charts Demo")

chart_data = pd.DataFrame(np.random.randn(20, 3), columns= ['A', 'B', 'C'])

st.subheader("Area Chart")
st.area_chart(chart_data)

st.subheader("Bar Chart")
st.bar_chart(chart_data)

st.subheader("Line Chart")
st.line_chart(chart_data)

st.subheader("Scatter Chart")
scatter_data = pd.DataFrame({
    'x': np.random.randn(100),
    'y': np.random.randn(100)
})