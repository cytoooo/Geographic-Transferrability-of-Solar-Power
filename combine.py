import pandas as pd

df_plant = pd.read_excel("datasets/Plant-1-4kwp-Combined.xlsx")
df_weather = pd.read_csv("datasets/Plant-1-Weather.csv")

# 1. Standardize and localize
df_plant['Time'] = pd.to_datetime(df_plant['Time'], errors='coerce')
df_plant['Time'] = df_plant['Time'].dt.tz_localize('Asia/Kolkata').dt.tz_convert('UTC')
df_weather['period_end'] = pd.to_datetime(df_weather['period_end'], utc=True, errors='coerce')
df_plant['Time'] = df_plant['Time'].dt.round('min')
df_weather['period_end'] = df_weather['period_end'].dt.round('min')

# 2. Merge
df_combined = pd.merge(
    df_plant[['Time','Production(kW)']],
    df_weather[['period_end', 'ghi', 'gti', 'dhi', 'dni', 'air_temp', 'cloud_opacity', 'wind_speed_10m','precipitation_rate','relative_humidity']],
    left_on='Time',
    right_on='period_end',
    how='inner'
)

# 3. Clean and sort
df_combined = df_combined.drop(columns=['period_end'])
df_combined = df_combined.sort_values(by=['Time'])

# 4. Convert back
df_combined['Time'] = df_combined['Time'].dt.tz_convert('Asia/Kolkata')

# 4. Format to string and export
df_combined['Time'] = df_combined['Time'].dt.strftime('%Y-%m-%d %H:%M:%S')
df_combined.to_excel("datasets/Plant-1-4kwp-Raw.xlsx", index=False)