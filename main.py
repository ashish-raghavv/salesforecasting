from fastapi import FastAPI
from fastapi.responses import JSONResponse
from forecast_logic import forecast_sales

app = FastAPI()

@app.get("/forecast")
def get_forecast():
    # Call the function with the cleaned daily CSV
    forecast_df = forecast_sales("daily_sales.csv")
    return JSONResponse(content=forecast_df.to_dict(orient="records"))

