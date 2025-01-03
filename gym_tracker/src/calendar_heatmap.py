import os
from datetime import datetime

import calplot
import matplotlib.pyplot as plt
import pandas as pd

all_days = pd.date_range("29-12-2024", datetime.today())

# read all csv files in the directory
files = [f for f in os.listdir("gym_tracker/private_data") if f.endswith(".csv")]
data = []
for file in files:
    df = pd.read_csv(f"gym_tracker/private_data/{file}")
    df["Date"] = file.split("_")[2].split(".")[0]
    data.append(df)
df = pd.concat(data)
df["Date"] = pd.to_datetime(df["Date"])
df = df.set_index("Date")
df = df.sort_index()

# group by date and sum the sets
df = df.groupby("Date").sum()

# Plot the calendar heatmap
calplot.calplot(
    df["Sets"],
    yearlabel_kws={"color": "black", "fontsize": 12},
    cmap="YlGn",
    edgecolor="black",
    vmin=15,
    vmax=df["Sets"].max(),
)
plt.show()
