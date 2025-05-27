# 🧠 Sales Forecasting App

A machine learning-powered web application that predicts future sales and explains the forecasts using LLM (Large Language Model) integration.

---

## 🚀 Features

- 📊 **Time Series Forecasting** using Facebook Prophet
- 🤖 **LLM-Based Explanation** of predictions (e.g., via ChatGPT/OpenAI API)
- ⚙️ **FastAPI Backend** with API endpoints for forecasts
- 🌐 **Streamlit or Frontend** to visualize the predictions
- 📁 CSV Uploads supported for custom sales data

---

## 📁 Project Structure

```
sales_forecasting_app/
│
├── backend/
│   ├── app.py               # FastAPI app and routes
│   ├── forecast_logic.py    # Forecasting logic using Prophet
│   ├── llm_explainer.py     # Generates explanations using OpenAI/GPT
│
├── frontend/
│   └── main.py              # Streamlit or frontend interface
│
├── utils/
│   └── helper_functions.py  # Utility functions (if any)
│
├── daily_sales.csv          # Example input data
├── stores_sales_forecasting.csv  # Example historical sales data
├── requirements.txt         # Python dependencies
└── README.md                # You’re here :)
```

---

## 📦 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/ashish-raghavv/salesforecasting.git
cd salesforecasting
```

### 2️⃣ Create Virtual Environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
```

### 3️⃣ Install Requirements
```bash
pip install -r requirements.txt
```

### 4️⃣ Run FastAPI Backend
```bash
uvicorn backend.app:app --reload
```

### 5️⃣ Run Streamlit Frontend (if available)
```bash
streamlit run frontend/main.py
```

---

## 📈 Example Usage

- Upload `daily_sales.csv` to forecast upcoming sales
- View charts in Streamlit
- Read a human-like explanation of the results from `llm_explainer.py`

---

## 🛠️ Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/)
- [Facebook Prophet](https://facebook.github.io/prophet/)
- [Streamlit](https://streamlit.io/)
- [OpenAI API](https://platform.openai.com/)
- Python 3.9+

---

## 👨‍💻 Author

**Ashish Raghav**  
📧 [ashishraghavv@gmail.com](mailto:ashishraghavv@gmail.com)  
🌐 [LinkedIn](https://www.linkedin.com/in/ashishraghavv/)

---

## 📃 License

This project is licensed under the MIT License.
