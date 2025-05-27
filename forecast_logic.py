from prophet import Prophet
import pandas as pd

def forecast_sales(df, periods=30):
    m = Prophet(daily_seasonality=True, yearly_seasonality=True)
    m.fit(df)
    future = m.make_future_dataframe(periods=periods)
    forecast = m.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
