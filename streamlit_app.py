import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("Advertising.csv")

df = load_data()
# Train model
df = df.drop(columns=["Unnamed: 0"])
@st.cache_resource
def train_model():
    X = df[['TV', 'Radio', 'Newspaper']]
    y = df['Sales']
    model = LinearRegression()
    model.fit(X, y)
    y_pred = model.predict(X)

    # Metrics
    rmse = np.sqrt(mean_squared_error(y, y_pred))
    r2 = r2_score(y, y_pred)
    return model, rmse, r2, y, y_pred, X.columns

model, rmse, r2, y_actual, y_pred, feature_names = train_model()

# UI
st.header("📊 Predict Sales from Ad Spend")
st.write("**Developed by: Kiran Salve**")
st.write("**Portfolio** : [Portfolio-Kiran Salve](https://kiran-salve-portfolio.vercel.app/)")

st.write("A simple **Machine Learning web app** built by with Streamlit that predicts product sales based on TV, Radio, and Newspaper advertising spend.  The model is trained using **Multiple Linear Regression** on the classic [Advertising dataset](https://www.kaggle.com/search?q=advertising+dataset)")


st.subheader("📈 Model Performance")
st.write(f"Model : Linear Regression")
st.write(f"- **RMSE:** {rmse:.2f}")
st.write(f"- **R² Score:** {r2:.2f}")

st.write(f"""
**RMSE (Root Mean Squared Error) = {rmse:.2f}**  
On average, our predictions are off by about **{rmse:.2f} units** of our target variable.  

**R² Score = {r2:.2f}**  
This means our model explains **{r2*100:.0f}% of the variance** in the target variable.  
The closer to 1, the better — so **{r2:.2f}** indicates the model fits the data very well.
""")

# Coefficients
st.subheader("📋 Model Coefficients")
coeff_df = pd.DataFrame({
    "Feature": feature_names,
    "Coefficient": model.coef_
})
st.write(coeff_df)
st.write(f"**Intercept:** {model.intercept_:.2f}")

# Plot Actual vs Predicted
st.subheader("📉 Actual vs Predicted Sales")
fig, ax = plt.subplots()
ax.scatter(y_actual, y_pred, color="blue", alpha=0.6, label="Predicted vs Actual")
ax.plot([y_actual.min(), y_actual.max()],
        [y_actual.min(), y_actual.max()],
        color="red", linestyle="--", label="Best Fit Line")
ax.set_xlabel("Actual Sales")
ax.set_ylabel("Predicted Sales")
ax.set_title("Actual vs Predicted Sales")
ax.legend()
st.pyplot(fig)

# Prediction UI
st.subheader("🔮 Make a Prediction")
tv = st.number_input("TV Spend", min_value=0.0)
radio = st.number_input("Radio Spend", min_value=0.0)
newspaper = st.number_input("Newspaper Spend", min_value=0.0)


if st.button("Predict"):
    new_data = [[tv, radio, newspaper]]
    predicted_sales = model.predict(new_data)[0]
    st.success(f"✅ Predicted Sales: ₹{round(predicted_sales, 2)} lakhs")

