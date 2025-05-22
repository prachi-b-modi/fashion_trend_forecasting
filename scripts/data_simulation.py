import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def generate_mock_data():
    dates = pd.date_range(end=datetime.today(), periods=90)
    styles = ["Y2K", "Boho", "Minimalist", "Gothcore", "Athleisure"]
    captions = [f"Love this new {style} look! #fashion" for style in styles]
    data = {
        "date": np.random.choice(dates, 500),
        "caption": np.random.choice(captions, 500)
    }
    df = pd.DataFrame(data)
    df = df.sort_values("date")
    return df
