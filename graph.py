import streamlit as st
import pandas as pd
import numpy as np

# line graph
chart_data = pd.DataFrame(np.floor(np.random.randn(20, 1)*10), columns=["col1"])

st.scatter_chart(
   chart_data  # Optional
)

print(chart_data)




