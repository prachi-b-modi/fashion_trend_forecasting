import pandas as pd
from prophet import Prophet

def forecast_keyword_trend(df):
    counts = df.groupby('date').size().reset_index(name='count')
    counts.columns = ['ds', 'y']
    m = Prophet()
    m.fit(counts)
    future = m.make_future_dataframe(periods=30)
    forecast = m.predict(future)
    return forecast, m
