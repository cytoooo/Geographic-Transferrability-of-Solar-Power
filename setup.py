import os
import glob
import pandas as pd
dataset_dir = "datasets/Plant-1-4kwp"
file_pattern = os.path.join(dataset_dir, "*.xlsx")
excel_files = glob.glob(file_pattern)
if not excel_files:
    raise FileNotFoundError(f"No .xlsx files found in {dataset_dir}")
dataframes = []
for file in excel_files:
    print(f"Reading: {os.path.basename(file)}")
    df = pd.read_excel(file)
    dataframes.append(df)
plant_data = pd.concat(dataframes, ignore_index=True)
print(f"Total rows in combined dataset: {len(plant_data)}")
plant_data.to_excel("datasets/Plant-1-4kwp-Combined.xlsx", index=False)