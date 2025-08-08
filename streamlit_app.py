import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import numpy as np

def train_model():
    df = pd.read_csv("Advertising.csv")
    X = df[['TV', 'Radio', 'Newspaper']]
    y = df['Sales']

    # Split into train & test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Predictions for test set
    y_pred = model.predict(X_test)
    
    model = LinearRegression()
    model.fit(X, y)
    
    # Metrics
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    metrics = {
        "RMSE": round(rmse, 2),
        "MAE": round(mae, 2),
        "R² Score": round(r2, 2)
    }

    return model,  metrics

model, metrics = train_model()

# UI
st.title("📊 Predict Sales from Ad Spend")


st.subheader("📈 Model Performance")
st.write(f"**RMSE:** {metrics['RMSE']}")
st.write(f"**MAE:** {metrics['MAE']}")
st.write(f"**R² Score:** {metrics['R² Score']}")

tv = st.number_input("TV Spend", min_value=0)
radio = st.number_input("Radio Spend", min_value=0)
newspaper = st.number_input("Newspaper Spend", min_value=0)


if st.button("Predict"):
    new_data = [[tv, radio, newspaper]]
    predicted_sales = model.predict(new_data)[0]
    st.success(f"✅ Predicted Sales: ₹{round(predicted_sales, 2)} lakhs")