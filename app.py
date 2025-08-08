import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

def train_model():
    df = pd.read_csv("Advertising.csv")
    X = df[['TV', 'Radio', 'Newspaper']]
    y = df['Sales']
    model = LinearRegression()
    model.fit(X, y)
    return model

model = train_model()

# UI
st.title("📊 Predict Sales from Ad Spend")

tv = st.number_input("TV Spend", min_value=0.0)
radio = st.number_input("Radio Spend", min_value=0.0)
newspaper = st.number_input("Newspaper Spend", min_value=0.0)

if st.button("Predict"):
    new_data = [[tv, radio, newspaper]]
    predicted_sales = model.predict(new_data)[0]
    st.success(f"✅ Predicted Sales: ₹{round(predicted_sales, 2)} lakhs")