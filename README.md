# 📊 Sales Prediction App — Linear Regression (Streamlit)

## 📝 Introduction
This is an **interactive Machine Learning web application** built using **Streamlit** that predicts **product sales** based on **advertising spend** on TV, Radio, and Newspaper.  
It’s designed to demonstrate my skills in:
- Data cleaning & analysis
- Model building with **scikit-learn**
- Deployment of ML models as interactive apps

📌 **Goal:** Make sales forecasting simple, fast, and accessible for marketing & sales teams.

---

## 🚀 Features
- **📥 Data Upload** — Upload CSV datasets for custom predictions
- **⚙️ Train & Predict** — Model automatically trains on advertising dataset
- **📈 Visualization** — Scatter plot of actual vs predicted sales
- **✍️ Manual Input Mode** — Enter TV, Radio, Newspaper spends to get instant prediction
- **📊 Coefficients & Insights** — See how much each ad channel influences sales
- **🌐 Web Deployment** — Runs directly in browser via Streamlit

---

## 🖼 Preview

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/3358921d-71a6-4f47-9ae4-96a1cb2d581c" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/0c5742fa-df4a-402d-a232-22ce46685bd6" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/4b63ad01-53ac-4642-982f-6e8747406ea8" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/47106940-cd11-485e-9d64-af801a287cc2" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/3e69384e-d415-4361-8b2b-f0c7fb21cb7c" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/4d68a4aa-5fe4-412d-9745-1063558faa63" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/67315dfa-10e2-4983-a3fb-9621d134c2d7" />

---

## 🗂 Project Structure

```text

advertising_linear_regression/
│
├── advertising.csv # Dataset
├── streamlit_app.py # Streamlit application code
├── requirements.txt # Python dependencies
├── README.md # Project documentation
└── screenshot.png # App preview image

```


---

## 🔧 Tech Stack
- **Python**: Pandas, NumPy, scikit-learn, Matplotlib
- **Framework**: Streamlit
- **Version Control**: Git & GitHub
- **Deployment**: Streamlit Cloud

---

## 📊 Model Details
- **Algorithm**: Linear Regression
- **Features Used**:
  - TV Spend
  - Radio Spend
  - Newspaper Spend
- **Target**: Sales
- **Performance Metrics**:
  - R² Score: ~0.90 (varies based on data)
  - Mean Squared Error (MSE) reported in-app

**Model Coefficients:**
- TV: `coef_tv`
- Radio: `coef_radio`
- Newspaper: `coef_newspaper`
- Intercept: `intercept_value`

*(Values are dynamically displayed in app)*

---

## 📌 How to Run Locally
1. **Clone Repository**
   ```bash
   git clone https://github.com/yourusername/advertising_linear_regression.git
   cd advertising_linear_regression



Install Dependencies

```pip install -r requirements.txt
```

Run App

```streamlit run streamlit_app.py```

Open in Browser — Streamlit will provide a local URL.


Deployment

This project is deployed on Streamlit Cloud.

Live - https://adspent.streamlit.app/

