import streamlit as st

global result
from main import prediction_pipeline
import pandas as pd

df = pd.read_csv('dataset/training_data.csv')
cols= df.columns
cols = cols[:-2]


some_dict = {}


for key,value in enumerate(cols):
    result = st.checkbox(f"{value}",key =key)

    some_dict[value] = int(result)


model = st.selectbox(
    'choose the model you prefer',
    ('decision_tree', 'gradient_boost', 'random_forest'))

st.write('You selected:', model);


if st.button("press"):

    print(dict)
    # st.write(some_dict)
    st.write(df['prognosis'].unique())
    disease = prediction_pipeline(some_dict,model)
    st.write("Prediction")
    st.write(disease)