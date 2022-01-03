import csv
import pandas as pd
import numpy as np

raw = pd.read_csv("articled.csv")

q_articles = raw["total_event"].sort_values("score", ascending=True)
output = q_articles[["title", "timestamp", "total_event", "url"]].head(20).values.tolist()