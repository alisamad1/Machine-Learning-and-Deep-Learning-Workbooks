import streamlit as st
import pandas as  pd
import numpy as np
## title of the application
st.title("Hello Streamlit")
## displaying a simple text
st.write("This is a simple text")

## Creating a dataframe
df = pd.DataFrame({
    'First Column ' : [1,2,3,4],
    "second Column": [10,20,30,40]
})
## display the Dataframe
st.write("here is our dataframe")
st.write(df)
 

## Now let us execute our Line Chart
chart_Data = pd.DataFrame(
    np.random.randn(20,3), columns=["a", "b", "c"]

)
st.line_chart(chart_Data)