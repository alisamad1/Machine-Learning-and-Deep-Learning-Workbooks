import streamlit as st
import pandas as pd
from sklearn.metrics import load_iris
from sklearn.ensemble import RandomForestClassifier


def load_data():
    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    df['species'] = iris.target
    return df, iris.target_names
df,target_names = load_data()
modl = RandomForestClassifier()
model.fit(df.iloc[:,:-1],df['species'])
st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Sepal Length ", float(df['Sepal Length (cm)'].min()),float(df['Sepal Length (cm)'].max()))
sepal_width = st.sidebar.slider("Sepal Width ", float(df['Sepal Width (cm)'].min()), float(df['Sepal Width (cm)'].max()))
petal_length = st.sidebar.slider("Petal Length ", float(df['Petal Length (cm)'].min()), float(df['Petal Length (cm)'].max()))
petal_width = st.sidebar.slider("Petal Width ", float(df['Petal Width (cm)' ].min()), float(df['Petal Width (cm)'].ma()))

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]
## Prediction of the model
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]