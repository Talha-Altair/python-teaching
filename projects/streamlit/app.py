import streamlit as st
import pandas as pd
import numpy as np

st.title("OUR PAGE")

st.write("hello world")
my_data = pd.DataFrame({
    'pineapple': [1, 2, 3, 4],
    'pizza': [10, 20, 30, 40]
})

st.write(my_data)

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['apples', 'bananas', 'oranges'])

st.line_chart(chart_data)



