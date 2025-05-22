import spacy
from collections import Counter
import pandas as pd

nlp = spacy.load("en_core_web_sm")

def extract_keywords(df):
    all_tokens = []
    for caption in df['caption']:
        doc = nlp(caption)
        all_tokens += [token.text.lower() for token in doc if token.pos_ in ["NOUN", "ADJ"]]
    freq = Counter(all_tokens)
    top_keywords = freq.most_common(10)
    return pd.DataFrame(top_keywords, columns=["keyword", "frequency"])
