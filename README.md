# Fashion Trend Forecasting

This project forecasts fashion trends using a mix of social media data (mocked) and computer vision + NLP. It applies basic image analysis and keyword extraction to detect style and trend evolution, with time-series forecasting using Prophet.

Scrape Instagram, TikTok, Pinterest, and fashion week images.

Use NLP on captions + computer vision on images to detect emerging trends.

Time series forecasting to predict which colors/styles will rise next season.

## Features
- Simulates scraping captions and fashion images
- Uses spaCy for keyword trend analysis
- Extracts dominant colors from images using OpenCV
- Forecasts trend keywords over time with Prophet
- Includes a simple Streamlit app for demo

## Run the notebook
```
jupyter notebook fashion_trend_forecasting.ipynb
```

## Run the app
```
streamlit run app.py
```
