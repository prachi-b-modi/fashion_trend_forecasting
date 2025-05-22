import streamlit as st
import pandas as pd
from scripts.data_simulation import generate_mock_data
from scripts.nlp_keyword_extraction import extract_keywords
from scripts.forecast_keywords import forecast_keyword_trend
import matplotlib.pyplot as plt

st.title("🧠 Fashion Trend Forecasting")

df = generate_mock_data()
st.write("### Sample Captions")
st.dataframe(df.head())

st.write("### Top Keywords")
keywords = extract_keywords(df)
st.bar_chart(keywords.set_index("keyword"))

st.write("### Forecasting Mentions Over Time")
forecast, model = forecast_keyword_trend(df)
fig = model.plot(forecast)
st.pyplot(fig)
