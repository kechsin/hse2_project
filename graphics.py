import matplotlib.pyplot as plt
import numpy as np
import pandas
import pandas as pd
import json


def normalize(series):
    return (series / series.sum()) * 100


clusters = ["music", "politics", "science", "art", "sport", "funny", "games"]
data = pandas.read_json("sentiment_data.json")
for col in data.columns:
    data[col] = normalize(data[col])

for i in clusters:
    axes = data.plot.pie(y=i, autopct='%1.1f%%')
    fig = axes.get_figure()
    fig.savefig(f"charts/pie_{i}.png")

data = data.transpose()
axes = data.plot.bar(stacked=True)
fig = axes.get_figure()
fig.savefig("charts/global_chart.png")


