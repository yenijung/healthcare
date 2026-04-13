import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv("data/insurance_updated.csv")

var = df.columns
print(var)

# baseline regression
df_model = df.copy()

X_base = df_model[['age', 'bmi', 'smoker_binary']]
y = df_model['charges']

X_train, X_test, y_train, y_test = train_test_split(X_base, y, test_size=0.2, random_state=42)

model_base = LinearRegression()
model_base.fit(X_train, y_train)

y_pred_base = model_base.predict(X_test)

rmse_base = np.sqrt(mean_squared_error(y_test, y_pred_base))
r2_base = r2_score(y_test, y_pred_base)

print("Baseline RMSE:", rmse_base)
print("Baseline R2:", r2_base)

# engineered regression
X_eng = df_model[['age', 'bmi', 'smoker_binary',
                  'smoker_bmi', 'bmi_30', 'smoker_bmi30', 'smoker_age']]

X_train, X_test, y_train, y_test = train_test_split(X_eng, y, test_size=0.2, random_state=42)

model_eng = LinearRegression()
model_eng.fit(X_train, y_train)

y_pred_eng = model_eng.predict(X_test)

rmse_eng = np.sqrt(mean_squared_error(y_test, y_pred_eng))
r2_eng = r2_score(y_test, y_pred_eng)

print("Engineered RMSE:", rmse_eng)
print("Engineered R2:", r2_eng)
