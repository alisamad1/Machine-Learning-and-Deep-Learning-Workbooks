import streamlit as st
import pandas as pd
st.title("streamlit text input")
name = st.text_input("Enter Your Name: ")
age = st.slider("Select your age: ",0,100,25)
st.write(f"Your age is {age}.")
options = ['Python', 'Java', 'C++', 'JavaScript']
choice = st.selectbox("Choose your favourite Language: ", options)
st.write(f"You selected {choice}.")
if name:
    st.write(f"Hello, {name}")
data = {
    "Name" : ["John", "Jake", "Jane", "Jill"],
    "Age" : [25, 30, 35, 40],
    "Gender" : ["Male", "Male", "Female", "Female"]
}
df = pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file = st.file_uploader("Choose a CSV file ", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)