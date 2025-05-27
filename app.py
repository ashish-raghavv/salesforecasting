import streamlit as st
import pandas as pd
from forecast_logic import forecast_sales

st.title("📈 Sales Forecasting App with Seasonality")

# Step 1: Upload CSV
uploaded_file = st.file_uploader("Upload your sales CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("CSV uploaded successfully!")
    st.write("📊 Input Data Preview", df.head())

    # Step 2: Forecast button
    if st.button("🔮 Predict Future Sales"):
        with st.spinner("Forecasting in progress..."):
            forecast = forecast_sales(df)
            st.success("Forecasting complete!")

            st.write("🔍 Forecast Preview", forecast.tail())

            # Step 3: Download button
            csv = forecast.to_csv(index=False)
            st.download_button("⬇️ Download Forecast CSV", csv, "forecast_output.csv", "text/csv")
