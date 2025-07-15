import pandas as pd
from glob import glob

def load_solar(path):
    df = pd.read_csv(path, skiprows=2)
    df["datetime"] = pd.to_datetime(dict(
        year=df["Year"],
        month=df["Month"],
        day=df["Day"],
        hour=df["Hour"]
    ))
    return df[["datetime", "GHI", "Temperature", "Relative Humidity"]]

def load_load(path):
    df = pd.read_csv(path)
    df["datetime"] = pd.to_datetime(df["Date"] + " " + (df["HR"] - 1).astype(str) + ":00")
    return df[["datetime", "CAISO"]]

# Load and Merge all Years
years = [2022, 2023, 2024]
merged = []

for year in years:
    solar = load_solar(f"data/solar_{year}.csv")
    load = load_load(f"data/load_{year}.csv")
    df = pd.merge(solar, load, on="datetime")
    merged.append(df)

# Concatenate all years
full_df = pd.concat(merged).sort_values("datetime").reset_index(drop=True)

# Label Grid Instability (Top 10% Load)
threshold = full_df["CAISO"].quantile(0.90)
full_df["grid_risk"] = (full_df["CAISO"] > threshold).astype(int)

# Save merged dataset
full_df.to_csv("data/merged.csv", index=False)
print(" Merged multi-year data saved to data/merged.csv")
print(f"Instability threshold: {threshold:.2f} MW")
print(full_df.head())
