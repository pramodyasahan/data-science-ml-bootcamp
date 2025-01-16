import streamlit as st
import pandas as pd
import numpy as np

st.title('Streamlit App')

# Display a Text
st.write("This is a text")

# Display a DataFrame
df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
st.write(df)

# Create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20, 3),columns=['a','b','c']
)
st.line_chart(chart_data)