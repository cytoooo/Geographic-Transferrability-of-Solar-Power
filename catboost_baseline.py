import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

from catboost import CatBoostRegressor

# 1. Load your finalized data
df = pd.read_excel("datasets/Plant-1-4kwp-Raw.xlsx")
print("Before removing NaNs: ", len(df))

# 2. Clean the data (Instantly drop any row containing a NaN value)
df = df.dropna()
print("After removing NaNs: ", len(df))

# 3. Define Features (X) and Target (y)
X = df.drop(columns=['Time', 'Production(kW)'])
y = df['Production(kW)']

# 4. Split into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 5. Initialize the Model
model = CatBoostRegressor(random_state=42, verbose=False, allow_writing_files=False)

# 6. Train the model
model.fit(X_train, y_train)

# 7. Make predictions
preds = model.predict(X_test)

# 8. Evaluate the results
max_actual = y_test.max()
rmse = mean_squared_error(y_test, preds) ** 0.5
rmse_pct = (rmse / max_actual) * 100
accuracy_pct = 100 - rmse_pct

print(f"RMSE: {rmse:.4f} kW")
print(f"Accuracy (100% - Error%): {accuracy_pct:.2f}%")

#93.28% accuracy